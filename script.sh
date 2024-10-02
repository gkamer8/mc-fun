#!/bin/bash

# Define paths
VENV_PATH="venv"
PYTHON_FILE="src/main.py"
RESULTS_DIR="results"

# Ensure the results directory exists
mkdir -p "$RESULTS_DIR"

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

# Run the Python script with the output file argument
python "$PYTHON_FILE" -o "$RESULTS_DIR" "$@"

# Deactivate the virtual environment
deactivate
