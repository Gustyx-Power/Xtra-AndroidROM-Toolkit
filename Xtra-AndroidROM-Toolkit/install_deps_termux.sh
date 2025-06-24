#!/data/data/com.termux/files/usr/bin/bash

echo "📦 Installing dependencies for Termux..."

pkg update -y && pkg upgrade -y
pkg install -y python clang libffi openssl zlib

# Upgrade pip
pip install --upgrade pip setuptools wheel

# Install requirements
pip install -r requirements.txt

echo "✅ All dependencies have been installed in Termux-Android."