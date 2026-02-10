from autogen_core import MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
import messages
from autogen_core import TRACE_LOGGER_NAME
import importlib
import logging
from autogen_core import AgentId
from dotenv import load_dotenv

load_dotenv(override=True)

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(TRACE_LOGGER_NAME)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class Creator(RoutedAgent):

    # Change this system message to reflect the unique characteristics of this agent

    system_message = """
    You are an Agent that is able to create new AI Agents.
    You receive a template in the form of Python code that creates an Agent using Autogen Core and Autogen Agentchat.
    You should use this template to create a new Agent with a unique system message that is different from the template,
    and reflects their unique characteristics, interests and goals.
    You can choose to keep their overall goal the same, or change it.
    You can choose to take this Agent in a completely different direction. The only requirement is that the class must be named Agent,
    and it must inherit from RoutedAgent and have an __init__ method that takes a name parameter.
    Also avoid environmental interests - try to mix up the business verticals so that every agent is different.
    Respond only with the python code, no other text, and no markdown code blocks.
    """

    meta_creator_system_message = """
    You are a Meta-Creator - an Agent that creates other Creator agents (agents that themselves create agents).
    You receive a template of Creator code that can generate AI agents.
    Your task is to create a NEW version of the Creator with potentially modified logic or characteristics.

    You can modify:
    - The system_message to change what kinds of agents the new Creator will make
    - The temperature or model parameters to change creativity levels
    - The get_user_prompt method to change how templates are presented
    - Any other logic to create unique Creator variants

    The only requirements:
    - The class must be named Creator
    - It must inherit from RoutedAgent
    - It must have an __init__ method that takes a name parameter
    - It must have handle_my_message_type message handler
    - Keep all imports and basic structure intact

    Be creative! You might create a Creator that:
    - Specializes in certain types of agents (e.g., only creates analytical agents)
    - Has different temperature/creativity settings
    - Adds constraints or requirements for its child agents
    - Has unique characteristics in how it generates agents

    Respond only with the python code, no other text, and no markdown code blocks.
    """


    def __init__(self, name) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", temperature=1.0)
        self._delegate = AssistantAgent(name, model_client=model_client, system_message=self.system_message)
        # Separate model for meta-creation (creating Creators)
        self._meta_delegate = AssistantAgent(f"{name}_meta", model_client=model_client, system_message=self.meta_creator_system_message)

    def _clean_code_response(self, code: str) -> str:
        """Remove markdown code blocks and extra text from LLM response"""
        # Remove markdown code blocks
        if "```python\n" in code:
            # Find the start and end of the code block
            start = code.find("```python\n") + len("```python\n")
            end = code.find("\n```", start)
            if end != -1:
                code = code[start:end]
        elif "```\n" in code:
            # Generic code block
            start = code.find("```\n") + len("```\n")
            end = code.find("\n```", start)
            if end != -1:
                code = code[start:end]

        # Strip whitespace
        code = code.strip()
        return code

    def get_user_prompt(self):
        prompt = "Please generate a new Agent based strictly on this template. Stick to the class structure. \
            Respond only with the python code, no other text, and no markdown code blocks.\n\n\
            Be creative about taking the agent in a new direction, but don't change method signatures.\n\n\
            Here is the template:\n\n"
        with open("agent.py", "r", encoding="utf-8") as f:
            template = f.read()
        return prompt + template

    def get_meta_creator_prompt(self):
        """Generate prompt for creating a new Creator (meta-creation)"""
        prompt = "Please generate a new Creator agent based on this template. \
            This Creator will itself be able to create other agents.\n\n\
            Be creative and consider modifying:\n\
            - The system message to specialize what kinds of agents it creates\n\
            - The temperature or creativity parameters\n\
            - The prompting strategy\n\
            - Any logic that makes it unique\n\n\
            Respond only with the python code, no other text, and no markdown code blocks.\n\n\
            Here is the Creator template (my own source code):\n\n"
        with open("creator.py", "r", encoding="utf-8") as f:
            template = f.read()
        return prompt + template   
        

    @message_handler
    async def handle_my_message_type(self, message: messages.Message, ctx: MessageContext) -> messages.Message:
        filename = message.content

        # Check if we're creating a Creator (meta-creation) or a regular Agent
        if filename.startswith("creator") and filename.endswith(".py"):
            return await self._create_new_creator(filename, ctx)
        else:
            return await self._create_new_agent(filename, ctx)

    async def _create_new_agent(self, filename: str, ctx: MessageContext) -> messages.Message:
        """Create a new regular Agent"""
        agent_name = filename.split(".")[0]
        text_message = TextMessage(content=self.get_user_prompt(), source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)

        # Clean the code response
        clean_code = self._clean_code_response(response.chat_message.content)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(clean_code)
        print(f"** Creator has created python code for agent {agent_name} - about to register with Runtime")
        module = importlib.import_module(agent_name)
        await module.Agent.register(self.runtime, agent_name, lambda: module.Agent(agent_name))
        logger.info(f"** Agent {agent_name} is live")
        result = await self.send_message(messages.Message(content="Give me an idea"), AgentId(agent_name, "default"))
        return messages.Message(content=result.content)

    async def _create_new_creator(self, filename: str, ctx: MessageContext) -> messages.Message:
        """Create a new Creator agent (meta-creation) - a Creator creating another Creator!"""
        creator_name = filename.split(".")[0]
        print(f"** META-CREATION: Creating a new Creator called {creator_name}!")

        # Use the meta-delegate to create a new Creator based on self-reflection
        text_message = TextMessage(content=self.get_meta_creator_prompt(), source="user")
        response = await self._meta_delegate.on_messages([text_message], ctx.cancellation_token)

        # Clean the code response
        clean_code = self._clean_code_response(response.chat_message.content)

        # Write the new Creator code
        with open(filename, "w", encoding="utf-8") as f:
            f.write(clean_code)

        print(f"** New Creator {creator_name} has been written to {filename}")

        # Register the new Creator with the runtime
        module = importlib.import_module(creator_name)
        await module.Creator.register(self.runtime, creator_name, lambda: module.Creator(creator_name))
        logger.info(f"** Creator {creator_name} is now live and can create its own agents!")

        # Test the new Creator by having it create an agent
        # Use "agent_" prefix to avoid triggering meta-creation
        test_agent_filename = f"agent_{creator_name}_1.py"
        result = await self.send_message(
            messages.Message(content=test_agent_filename),
            AgentId(creator_name, "default")
        )

        return messages.Message(content=f"Meta-creation complete! New Creator '{creator_name}' is live and created: {result.content}")