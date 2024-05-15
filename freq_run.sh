#!/bin/bash

# Prompt user for input
read -p "Enter document URL: " DOC_URL
read -p "Enter start rank: " START_RANK
read -p "Enter end rank: " END_RANK

# Run the Python script with the inputs as arguments
python3 src/wordfreq.py "$DOC_URL" "$START_RANK" "$END_RANK"
