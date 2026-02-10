# Setup Guide

## Step 1: Install Dependencies

The dependencies have been installed! ✅

```bash
python3 -m pip install -r requirements.txt
```

## Step 2: Set Up Your OpenAI API Key

You need to create a `.env` file with your OpenAI API key.

### Option A: Create .env file manually

```bash
# Create .env file
cat > .env << EOF
OPENAI_API_KEY=your_actual_api_key_here
EOF
```

Replace `your_actual_api_key_here` with your actual OpenAI API key.

### Option B: Copy from template

```bash
# Copy template
cp .env.template .env

# Edit the file
nano .env
# (or use any text editor to add your API key)
```

### Where to Get Your API Key

1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy it to your `.env` file

## Step 3: Run the Demo

Once you have your `.env` file set up:

```bash
# Simple test (recommended first)
python3 simple_meta_test.py

# Chain test
python3 simple_meta_test.py chain

# Full demo
python3 meta_world.py

# Original functionality
python3 world.py
```

## Troubleshooting

### "No module named 'autogen_ext'"
```bash
python3 -m pip install -r requirements.txt
```

### "No API key found"
- Make sure you created the `.env` file
- Make sure it contains: `OPENAI_API_KEY=sk-...`
- Make sure the `.env` file is in the same directory as the scripts

### "Connection refused"
- Each script uses a different port
- If you see connection errors, make sure no other script is running
- Try a different script (they use different ports):
  - simple_meta_test.py uses port 50053
  - meta_world.py uses port 50052
  - world.py uses port 50051

## Verify Installation

```bash
# Check Python version (should be 3.8+)
python3 --version

# Check if packages are installed
python3 -c "import autogen_core; import autogen_agentchat; import autogen_ext; print('All packages installed!')"

# Check if .env exists
cat .env
```

## Next Steps

Once setup is complete:
1. Read [README_META.md](README_META.md) for overview
2. Read [QUICKSTART_META.md](QUICKSTART_META.md) for usage
3. Run `python3 simple_meta_test.py` to see meta-creation in action!
