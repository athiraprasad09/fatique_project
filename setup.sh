#!/bin/bash

# Cognitive Fatigue Detector - Quick Start Script
# Developed by Bread Butter Club

set -e

echo "🧠 Cognitive Fatigue Detector - Deployment Setup"
echo "================================================"
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python 3 detected: $(python3 --version)"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Train model
echo "🤖 Training ML model..."
python train.py

# Success message
echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 To start the application:"
echo "   1. Activate virtual environment: source venv/bin/activate"
echo "   2. Start backend: python app.py"
echo "   3. Open index.html in your browser"
echo ""
echo "📖 For deployment guides, see DEPLOYMENT.md"
echo ""
echo "Developed by Bread Butter Club 🍞🧈"
