#!/bin/bash

# Prompt user for input
read -p "Enter input: " USER_INPUT

# Run the Python script with the input as an argument
python3 src/textgen.py "$USER_INPUT"
