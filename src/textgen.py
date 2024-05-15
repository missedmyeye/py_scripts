"""The purpose of this script is to generate text from a LLM with a given text.

Returns:
    generated_text (str): continuated text 
"""
import os
import json
from dotenv import load_dotenv
import requests
import sys

# Step 1: Read configuration parameters from the file
config = {}
with open("gen_config.json", 'r') as file:
    config = json.load(file)[0]

API_URL = config.get("API_URL")

# Read input from command-line argument, default to config value if no input
if len(sys.argv) > 1 and sys.argv[1].strip():
    INPUT_STR = sys.argv[1]
else:
    INPUT_STR = config.get("input")

# Load environment variables from .env file
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    """Sends a POST request to provided API_URL and returns the response
    in JSON dict format, enclosed in square brackets.

    Args:
        payload (dict): inputs and other parameters to be submitted to API
        Example:
        {
        "inputs": "Life is a box of",
        "max_new_tokens":50,
        "num_return_sequences":1,
        "temperature":0.1
        }

    Returns:
        response.json(): response from API
        Example:
        [{'generated_text': 'Life is a box of cards that you may find interesting, 
        or some random action on the box that you may be able to take to make a 
        character. Once a character is learned, they become a part of your 
        story for a few days. They'}]

    """
    response = requests.post(API_URL, headers=headers, json=payload)
    
    return response.json()

data = query(
    {
        "inputs": INPUT_STR,
        "max_new_tokens":config.get("max_new_tokens"),
        "num_return_sequences":config.get("num_return_sequences"),
        "temperature":config.get("temperature")
        }
    )

generated_text = data[0]['generated_text']

final_output = f"Input: {INPUT_STR}\nGenerated Text: {generated_text}"

print(final_output)