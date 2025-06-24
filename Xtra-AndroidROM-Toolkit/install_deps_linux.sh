#!/bin/bash

echo "📦 Installing dependencies for Linux..."

sudo apt update && sudo apt install -y \
    python3 python3-pip python3-dev\
    build-essential libffi-dev libssl-dev zlib1g-dev

# Upgrade pip
python3 -m pip install --upgrade pip setuptools wheel

# Install requirements
python3 -m pip install -r requirements.txt

echo "✅ All dependencies have been installed on Linux."