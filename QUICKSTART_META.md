# Quick Start: Meta-Creation 🚀

## What You're About to See

You're going to witness AI agents creating AI agents that create AI agents. Mind-bending? Yes. Cool? Absolutely.

## Prerequisites

1. Install dependencies:
```bash
pip install autogen-core autogen-agentchat autogen-ext python-dotenv
```

2. Set up your `.env` file with OpenAI API key:
```bash
OPENAI_API_KEY=your_key_here
```

## Option 1: Simple Test (Recommended for First Time)

Create ONE new Creator and see it in action:

```bash
python simple_meta_test.py
```

This will:
- ✅ Original Creator reads its own code (`creator.py`)
- ✅ Creates a specialized Creator variant (`creator_specialist.py`)
- ✅ New Creator creates its own agent (`creator_specialist_agent1.py`)
- ✅ Returns the result

**Expected Output:**
```
================================================================================
SIMPLE META-CREATION TEST
================================================================================

Step 1: Original Creator reads its own code (creator.py)
Step 2: Original Creator creates a specialized Creator
Step 3: New Creator creates its own agent

** META-CREATION: Creating a new Creator called creator_specialist!
** New Creator creator_specialist has been written to creator_specialist.py
** Creator creator_specialist is now live and can create its own agents!

✓ Check these files:
  - creator_specialist.py (the new Creator)
  - creator_specialist_agent1.py (agent created by the new Creator)
  - meta_test_result.md (detailed result)
```

## Option 2: Chain Test (Advanced)

See a Creator create a Creator that creates a Creator:

```bash
python simple_meta_test.py chain
```

This creates a 3-generation chain:
```
Creator → Creator2 → Creator3 → Agent
```

## Option 3: Full Demo (Multiple Variants)

Create multiple Creator variants at once:

```bash
python meta_world.py
```

This creates:
- `creator_analytical.py` - Specializes in analytical agents
- `creator_creative.py` - Specializes in creative agents
- `creator_experimental.py` - Highly experimental approach

Each new Creator immediately creates its own agent to demonstrate it works!

## Option 4: Regular Agent Creation (Original Functionality)

Still want to create regular agents?

```bash
python world.py
```

This creates 20 regular business idea agents (the original functionality).

## Understanding the Output

### Files Created

#### New Creators (Meta-Creation)
- `creator_*.py` - New Creator variants
- Each can create agents!

#### Agents Created by New Creators
- `creator_*_agent1.py` - Proof that new Creators work

#### Result Files
- `*_result.md` - Detailed results of what was created

### Example Creator Variant

Here's what a specialized Creator might look like:

```python
class Creator(RoutedAgent):
    # Modified system message for specialization
    system_message = """
    You are an Agent Creator specializing in ANALYTICAL agents.
    Create agents focused on data analysis, strategic thinking,
    and logical reasoning...
    """

    def __init__(self, name) -> None:
        super().__init__(name)
        # Maybe lower temperature for more focused output
        model_client = OpenAIChatCompletionClient(
            model="gpt-4o-mini",
            temperature=0.3  # ← Changed from 1.0!
        )
        # ... rest of the code
```

## Inspecting the Results

### Check the Generated Code

```bash
# See the new Creator
cat creator_specialist.py

# See the agent it created
cat creator_specialist_agent1.py

# See the result
cat meta_test_result.md
```

### Compare to Original

```bash
# Original Creator
cat creator.py

# New Creator variant
cat creator_analytical.py

# What changed?
diff creator.py creator_analytical.py
```

## Troubleshooting

### "No module named 'creator_X'"

Make sure the Creator was successfully created before trying to use it:
```bash
ls creator_*.py
```

### "Connection refused" or Runtime errors

Each script uses a different port. If you see connection errors:
1. Make sure no other script is running
2. Check if the port is already in use
3. Try a different script (they use different ports)

### "API key not found"

Set your OpenAI API key:
```bash
export OPENAI_API_KEY=your_key_here
```

Or add to `.env` file:
```
OPENAI_API_KEY=your_key_here
```

## What to Look For

### In the New Creator Code

1. **Modified System Message**
   - Does it specialize in certain types of agents?
   - Is the personality different?

2. **Changed Parameters**
   - Temperature: Higher = more creative, Lower = more focused
   - Model: Different model for different capabilities?

3. **Logic Modifications**
   - Different prompting strategy?
   - Additional constraints?
   - Unique characteristics?

### In the Created Agent

1. **Does it reflect the Creator's specialization?**
   - Analytical Creator → Analytical Agent?
   - Creative Creator → Creative Agent?

2. **Quality of output**
   - Is the business idea coherent?
   - Does it match the intended style?

## Next Steps

### Experiment!

1. **Create your own Creator variant**
   ```bash
   python simple_meta_test.py
   # Then modify creator_specialist.py manually
   ```

2. **Chain multiple generations**
   ```bash
   python simple_meta_test.py chain
   # See how traits evolve across generations
   ```

3. **Compare different variants**
   ```bash
   python meta_world.py
   # Compare analytical vs creative vs experimental
   ```

### Modify the Code

1. **Change the meta_creator_system_message**
   - Edit `creator.py` line 36-61
   - Modify what kinds of variants are created

2. **Add more specializations**
   - Edit `meta_world.py` creator_variants list
   - Create domain-specific Creators

3. **Implement fitness functions**
   - Rate Creator effectiveness
   - Evolve toward better Creators

## Going Deeper

### Read the Architecture

```bash
cat ARCHITECTURE.md
```

### Understand the Philosophy

```bash
cat META_CREATION.md
```

### Study the Code

Key files to understand:
1. `creator.py` (lines 80-147) - Meta-creation logic
2. `messages.py` - How agents communicate
3. `agent.py` - Template that gets varied

## Fun Ideas to Try

1. **Create a Creator that creates only silly agents**
2. **Make a Creator that's extremely conservative vs one that's wild**
3. **Create a Creator that specializes in a specific industry**
4. **Chain 5+ generations and see what emerges**
5. **Have two Creator lineages compete**

## Questions?

Check out:
- `META_CREATION.md` - Philosophical overview
- `ARCHITECTURE.md` - Technical details
- `creator.py` - The actual implementation

---

**Remember:** You're not just creating agents. You're creating creators of agents. You're basically playing God, but with code. Have fun! 🧬🤖✨
