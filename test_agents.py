"""
Simple test to create regular agents (not Creators)
This is faster than meta-creation
"""

from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntimeHost
from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntime
from creator import Creator
from autogen_core import AgentId
import messages
import asyncio


async def create_agents():
    """Create several regular agents"""
    host = GrpcWorkerAgentRuntimeHost(address="localhost:50055")
    host.start()
    worker = GrpcWorkerAgentRuntime(host_address="localhost:50055")
    await worker.start()

    # Register the Creator
    await Creator.register(worker, "Creator", lambda: Creator("Creator"))
    creator_id = AgentId("Creator", "default")

    print("\n" + "="*60)
    print("CREATING 5 REGULAR AGENTS")
    print("="*60)

    # Create 5 agents
    for i in range(1, 6):
        filename = f"agent{i}.py"
        print(f"\n📝 Creating {filename}...")

        try:
            result = await worker.send_message(
                messages.Message(content=filename),
                creator_id
            )

            print(f"✅ Created {filename}")
            print(f"💡 Idea: {result.content[:100]}...")

            # Save the idea
            with open(f"idea{i}.md", "w") as f:
                f.write(f"# Agent {i} Business Idea\n\n")
                f.write(result.content)

        except Exception as e:
            print(f"❌ Error creating {filename}: {e}")

    print("\n" + "="*60)
    print("DONE! Created 5 agents.")
    print("="*60)
    print("\nGenerated files:")
    print("  - agent1.py through agent5.py")
    print("  - idea1.md through idea5.md")

    try:
        await worker.stop()
        await host.stop()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(create_agents())
