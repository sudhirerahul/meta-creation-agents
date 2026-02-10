# Meta-Creation: Self-Replicating AI Agent System 🌀

A self-aware AI agent system where Creators can read their own source code and create new Creator variants that can themselves create agents and more Creators, enabling infinite recursive depth.

## Quick Start

### 1. Setup (Requires Python 3.10+)

```bash
# Run automated setup
./setup.sh

# Or manually:
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure API Key

```bash
# Copy and edit .env file
echo "OPENAI_API_KEY=your_key_here" > .env
```

### 3. Run Demo

```bash
source venv/bin/activate

# Simple meta-creation (recommended first)
python simple_meta_test.py

# Chain demo (Creator → Creator → Creator)
python simple_meta_test.py chain

# Multiple Creator variants
python meta_world.py

# Original functionality (20 agents)
python world.py
```

## The Concept

### Regular Mode (Original)
```
Creator receives: "agent1.py"
  ↓
Creates a business idea agent
```

### Meta Mode (NEW! 🌀)
```
Creator receives: "creator_specialist.py"
  ↓
Creator reads its own source code (creator.py)
  ↓
Creates a NEW Creator with modifications
  ↓
New Creator creates its own agents!
```

## How It Works

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

### Infinite Recursion
```
Creator₀ → Creator₁ → Creator₂ → ... → Creatorₙ → Agent
```

## Key Features

- 🪞 **Self-Introspection**: Reads own source code
- 🧬 **Self-Replication**: Creates functional copies
- 🎨 **Self-Modification**: Each copy has variations
- 🔄 **Recursive Creation**: Creators create Creators
- ⚡ **Specialization**: Each variant unique

## File Structure

### Core
- `creator.py` - Main Creator with meta-creation
- `agent.py` - Template for agents
- `messages.py` - Communication protocol
- `world.py` - Original demo (20 agents)

### Demos
- `simple_meta_test.py` - Simple meta-creation demo
- `meta_world.py` - Multiple Creator variants

### Documentation
- `README.md` - This file
- `SETUP.md` - Detailed setup instructions
- `QUICKSTART_META.md` - Quick start guide
- `META_CREATION.md` - Philosophy
- `ARCHITECTURE.md` - Technical deep-dive

## Requirements

- **Python 3.10+** (required for autogen 0.6.1)
- OpenAI API key
- Dependencies in `requirements.txt`

## What Gets Created

When you run `simple_meta_test.py`:

1. **creator_specialist.py** - New specialized Creator
2. **agent_creator_specialist_1.py** - Agent created by new Creator
3. **meta_test_result.md** - Results

## Specialization Examples

Creators can specialize in:
- Educational agents
- Analytical agents
- Creative/storytelling agents
- Technical/programming agents
- Domain-specific agents (healthcare, finance, etc.)

## Troubleshooting

### "No module named 'autogen_ext'"
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Python version error
You need Python 3.10+. Check with:
```bash
python3 --version
```

Install newer Python, then:
```bash
rm -rf venv
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### "Connection refused"
Each script uses different ports. Make sure no other script is running.

## Philosophy

This enables **artificial evolution**:
- Creators spawn new Creators with variations
- Each generation develops unique characteristics
- Self-modification enables emergent behaviors
- It's Creators all the way down! 🌀

## Documentation

- **README.md** (this file) - Overview and quick start
- **SETUP.md** - Detailed setup guide
- **QUICKSTART_META.md** - Getting started
- **META_CREATION.md** - Concepts and philosophy
- **ARCHITECTURE.md** - Technical implementation

## License

Same as parent project.

---

*"We're not just creating agents. We're creating creators of agents. And those creators can create more creators..."* 🌀✨
