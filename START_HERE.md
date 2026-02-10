# 🌀 Meta-Creation System - Start Here!

## What Is This?

A self-replicating AI agent system where **Creators create Creators** that can create agents, enabling infinite recursive depth and artificial evolution.

## Quick Start (3 Steps)

### 1️⃣ Setup
```bash
./setup.sh
```

### 2️⃣ Add API Key
```bash
# Edit .env and add your OpenAI API key
echo "OPENAI_API_KEY=sk-your-key-here" > .env
```

### 3️⃣ Run Demo
```bash
source venv/bin/activate
python simple_meta_test.py
```

## What Just Happened?

1. **Original Creator** read its own source code (`creator.py`)
2. **Created a specialized Creator** (`creator_specialist.py`)
3. **New Creator created its own agent** (`agent_creator_specialist_1.py`)

🌀 **Meta-creation complete!** The new Creator can now create more Creators or agents!

## Next Steps

### Try Different Demos
```bash
# Chain: Creator → Creator → Creator
python simple_meta_test.py chain

# Multiple variants at once
python meta_world.py

# Original: 20 business idea agents
python world.py
```

### Learn More
- **README.md** - Full overview
- **QUICKSTART_META.md** - Detailed examples
- **META_CREATION.md** - Philosophy
- **ARCHITECTURE.md** - How it works
- **FILES.md** - File overview

## Requirements

- Python 3.10+ (we set up Python 3.12 venv)
- OpenAI API key
- That's it!

## The Magic

```python
# Just change the filename!
"agent1.py"    → Creates an agent
"creator1.py"  → Creates a Creator! 🌀
```

## Troubleshooting

### Virtual environment not activated?
```bash
source venv/bin/activate
```

### Missing API key?
```bash
# Check .env file exists and has your key
cat .env
```

### Need help?
Check **SETUP.md** for detailed instructions.

---

**Ready? Run the demo!**
```bash
source venv/bin/activate && python simple_meta_test.py
```

🎉 **Enjoy creating Creators that create Creators!** 🌀
