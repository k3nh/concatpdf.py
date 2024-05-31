#!/bin/bash

# Check if uv is installed
if ! command -v uv &> /dev/null; then
  echo "uv is not installed. Please install it manually:"
  echo "Visit https://github.com/astral-sh/uv for installation instructions."
  exit 1
fi

# Create a virtual environment
uv venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install PyPDF2 within the virtual environment
uv pip install PyPDF2

# Deactivate the virtual environment (optional)
deactivate
