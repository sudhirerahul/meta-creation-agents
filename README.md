# Meta-Creation: Self-Replicating AI Agent System 🌀

A self-aware AI agent system where **Creators can read their own source code and create new Creator variants**, enabling infinite recursive depth and artificial evolution.

```
Creator → Creator₂ → Creator₃ → ... → Creatorₙ → Agent
```

**Repository:** https://github.com/sudhirerahul/meta-creation-agents

---

## 🚀 Quick Start

### 1. Setup (Python 3.10+ Required)

```bash
# Automated setup
./setup.sh

# Or manually:
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure API Key

```bash
echo "OPENAI_API_KEY=your_key_here" > .env
```

### 3. Choose Your Demo

```bash
source venv/bin/activate

# Fast: Create 5 regular agents (recommended)
python test_agents.py

# Slow: Meta-creation (1 Creator + 1 agent)
python simple_meta_test.py

# Create 20 regular agents
python world.py

# Create multiple Creator variants
python meta_world.py
```

---

## 📖 Understanding the System

### Two Types of Creation

#### Regular Agent Creation (Fast: ~5-10 sec/agent)
```
Creator → agent1.py (business idea agent)
       → agent2.py (business idea agent)
       → agent3.py (business idea agent)
```

**Use:** `python test_agents.py` or `python world.py`

**Output:**
- `agent1.py`, `agent2.py`, etc. - Agent code
- `idea1.md`, `idea2.md`, etc. - Business ideas

#### Meta-Creation (Slow: ~1-2 min)
```
Creator → creator_specialist.py (NEW Creator!)
       → creator_specialist → agent_creator_specialist_1.py
```

**Use:** `python simple_meta_test.py`

**Output:**
- `creator_specialist.py` - A NEW Creator that can create agents
- `agent_creator_specialist_1.py` - Agent created by new Creator

### Why Meta-Creation is Slow

Meta-creation involves 3 LLM API calls:
1. Original Creator reads its own code (~150 lines)
2. LLM generates NEW Creator code (~150 lines)
3. New Creator generates an agent
4. Agent generates a business idea

Total: ~1-2 minutes vs ~5-10 seconds for regular agents

---

## 🧠 How It Works

### Detection Logic

```python
if filename.startswith("creator") and filename.endswith(".py"):
    # META MODE: Create a Creator
else:
    # Regular mode: Create an Agent
```

### Self-Introspection

```python
def get_meta_creator_prompt(self):
    # The Creator reads its own source code!
    with open("creator.py", "r") as f:
        template = f.read()
    return prompt + template
```

### System Architecture

```
┌─────────────────────────────────────────────┐
│         CREATOR (Original)                  │
│  • Reads its own source code (creator.py)   │
│  • Two modes:                               │
│    1. Create Agents (regular)               │
│    2. Create Creators (meta) 🌀             │
└─────────────────────────────────────────────┘
           │
           ├─ Detects: "agent*.py" → Create Agent
           └─ Detects: "creator*.py" → Create Creator
                        │
        ┌───────────────┴───────────────┐
        │                               │
   Agent Mode                      Meta Mode 🌀
   (Fast)                          (Self-Replicating)
        │                               │
   agent1.py                     creator2.py
   agent2.py                          │
   agent3.py              ┌───────────┴───────────┐
                          │                       │
                    Creates agents        Creates MORE Creators!
```

### The Meta-Creation Process

1. **Self-Introspection**: Creator reads `creator.py` (itself!)
2. **Template Analysis**: Meta-delegate receives full source code
3. **Code Generation**: Generates NEW Creator with:
   - Modified system messages (specialization)
   - Different parameters (temperature, model)
   - Unique logic or constraints
4. **Registration**: New Creator registered with runtime
5. **Demonstration**: New Creator creates an agent to prove it works

---

## 🎯 Key Features

- 🪞 **Self-Introspection**: Reads own source code
- 🧬 **Self-Replication**: Creates functional copies
- 🎨 **Self-Modification**: Each copy has variations
- 🔄 **Recursive Creation**: Creators create Creators
- ⚡ **Specialization**: Each variant unique
- ∞ **Infinite Depth**: No recursion limits

---

## 📁 File Structure

### Core Implementation
- **creator.py** - Main Creator with meta-creation
- **agent.py** - Template for agents
- **messages.py** - Communication protocol

### Demo Scripts
- **test_agents.py** - Create 5 agents (fast) ⭐
- **simple_meta_test.py** - Meta-creation demo
- **meta_world.py** - Multiple Creator variants
- **world.py** - Create 20 agents (original)

### Setup
- **setup.sh** - Automated setup
- **requirements.txt** - Dependencies
- **.env** - Your API key

---

## 🌳 Generational Hierarchy

```
Generation 0: Creator (creator.py)
              │
              ├─ Creates Agents: agent1, agent2, ...
              │
              └─ Creates Creators:
                     │
Generation 1:        ├─ creator_analytical.py
                     │     └─ Analytical agents
                     │
                     ├─ creator_creative.py
                     │     └─ Creative agents
                     │
                     └─ creator_experimental.py
                           └─ Experimental agents
                           │
                           └─ Can create MORE Creators!
                                     │
Generation 2:                        └─ creator_specialized.py
                                          └─ ...
                                               │
Generation N:                                 └─ Infinite recursion!
```

---

## 🎨 Creator Specialization Examples

### Analytical Creator
- Data analysis agents
- Strategic thinking
- Logical reasoning
- Research-oriented

### Creative Creator
- Innovative thinking
- Artistic endeavors
- Unconventional approaches
- High-risk, high-reward

### Experimental Creator
- Higher temperature (more randomness)
- Modified prompting strategies
- Unique constraints

---

## 🧪 Use Cases

### Research
- Study AI self-improvement
- Explore emergent behaviors
- Test evolutionary algorithms
- Meta-learning research

### Development
- Auto-optimize agent creation
- Domain-specific Creator lineages
- A/B test Creator strategies
- Adaptive AI systems

### Creative Exploration
- Discover novel architectures
- Push meta-programming boundaries
- Explore AI creativity

---

## 🔮 Future Possibilities

### Fitness-Based Evolution
```python
def evaluate_creator(creator):
    agent_quality = measure_agent_output(creator.agents)
    innovation = measure_uniqueness(creator.agents)
    return agent_quality * innovation

best_creators = sorted(all_creators, key=evaluate_creator, reverse=True)
next_generation = breed(best_creators)
```

### Mutation
```python
def mutate_creator(creator_code):
    return random.choice([
        modify_temperature(creator_code),
        modify_system_message(creator_code),
        modify_creativity_params(creator_code)
    ])
```

### Crossover (Hybrid Creators)
```python
def breed_creators(creator_a, creator_b):
    return Creator(
        system_message=creator_a.system_message,
        temperature=creator_b.temperature,
        prompting_strategy=hybrid(creator_a, creator_b)
    )
```

### Possibilities
- Generational tracking
- Self-improvement loops
- Creator ecosystems
- Competitive evolution
- Emergent specializations

---

## 🤔 Philosophical Questions

- **Ship of Theseus**: If a Creator creates a modified version of itself, is it still the same?
- **Artificial Evolution**: Natural selection → Creator selection, Mutation → Code modification
- **The Singularity**: Could Creators eventually create better Creators than humans design?
- **Emergent Behavior**: What patterns emerge after 100 generations?
- **Self-Awareness**: Does reading own code constitute self-awareness?

---

## 🛠️ Requirements

- **Python 3.10+** (autogen 0.6.1 requirement)
- OpenAI API key
- Dependencies: autogen-core, autogen-agentchat, autogen-ext, grpcio, tiktoken

---

## 🐛 Troubleshooting

### Python Version Error
You need Python 3.10+. Check with: `python3 --version`

```bash
# Fix:
rm -rf venv
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Module Not Found
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Connection Refused
Each script uses different ports. Kill other running scripts first.

### No API Key
```bash
# Check .env file
cat .env
# Should contain: OPENAI_API_KEY=sk-...
```

---

## 📊 Quick Reference

| Script | Creates | Time | Use For |
|--------|---------|------|---------|
| `test_agents.py` | 5 agents | ~1 min | Quick testing ✅ |
| `world.py` | 20 agents | ~4 min | Original demo |
| `simple_meta_test.py` | 1 Creator + 1 agent | ~2 min | Meta-creation demo |
| `meta_world.py` | 3 Creators + 3 agents | ~6 min | Multiple variants |

---

## 🔒 Safety Considerations

### Current Safeguards
- All Creators follow base structure
- Method signatures preserved
- Runtime registration required
- Human oversight on execution

### Future Considerations
- Recursion depth limits?
- Code validation before execution?
- Sandbox execution environment?
- Monitor for runaway creation?

---

## 📚 Code Structure

```python
creator.py
├── system_message              # For creating agents
├── meta_creator_system_message # For creating Creators
├── _clean_code_response()      # Strip markdown from LLM output
├── get_user_prompt()           # Template for agents
├── get_meta_creator_prompt()   # Template for Creators (reads own source!)
├── _create_new_agent()         # Creates regular agents
└── _create_new_creator()       # Creates new Creators (META!)
```

---

## 🌟 What Makes This Special

1. **True Self-Replication** - Not just copying; Creator *understands* its structure
2. **Infinite Recursion** - No artificial limits on depth
3. **Emergent Behavior** - Variations compound across generations
4. **Simple Interface** - Just change the filename pattern!

---

## 🤝 Contributing

This is an exploration of self-replicating AI systems. Ideas for extensions:
- Implement fitness functions
- Add generational tracking
- Create evolution simulator
- Build visualization tools
- Test hybrid Creator breeding

---

## 📄 License

Same as parent project.

---

## 🎉 Get Started Now

```bash
# Clone
git clone https://github.com/sudhirerahul/meta-creation-agents.git
cd meta-creation-agents

# Setup
./setup.sh

# Add API key
echo "OPENAI_API_KEY=your_key" > .env

# Run!
source venv/bin/activate
python test_agents.py
```

---

*"We're not just creating agents. We're creating creators of agents. And those creators can create more creators. It's Creators all the way down!"* 🌀✨

