#!/bin/bash
# Setup script for meta-creation system

echo "=================================="
echo "Meta-Creation System Setup"
echo "=================================="
echo ""

# Check Python version
if ! command -v python3.12 &> /dev/null && ! command -v python3.11 &> /dev/null && ! command -v python3.10 &> /dev/null; then
    echo "❌ Error: Python 3.10 or higher required"
    echo "Please install Python 3.10+ first"
    exit 1
fi

# Find the best Python version
if command -v python3.12 &> /dev/null; then
    PYTHON=python3.12
elif command -v python3.11 &> /dev/null; then
    PYTHON=python3.11
else
    PYTHON=python3.10
fi

echo "✅ Found $PYTHON ($($PYTHON --version))"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
$PYTHON -m venv venv
echo "✅ Virtual environment created"
echo ""

# Activate and install dependencies
echo "Installing dependencies..."
source venv/bin/activate
pip install -q --upgrade pip
pip install -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  No .env file found"
    echo ""
    echo "Creating .env template..."
    cat > .env << EOF
# Add your OpenAI API key here
OPENAI_API_KEY=your_openai_api_key_here
EOF
    echo "✅ .env template created"
    echo ""
    echo "📝 IMPORTANT: Edit .env and add your OpenAI API key!"
    echo "   Get your key from: https://platform.openai.com/api-keys"
else
    echo "✅ .env file exists"
fi

echo ""
echo "=================================="
echo "Setup Complete! 🎉"
echo "=================================="
echo ""
echo "To activate the virtual environment:"
echo "  source venv/bin/activate"
echo ""
echo "To run the demos:"
echo "  source venv/bin/activate"
echo "  python simple_meta_test.py        # Simple demo"
echo "  python simple_meta_test.py chain  # Chain demo"
echo "  python meta_world.py              # Full demo"
echo ""
