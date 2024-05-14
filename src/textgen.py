"""The purpose of this script is to generate text from a LLM with a given text.

Returns:
    generated_text (str): continuated text 
"""
import os
from dotenv import load_dotenv
import requests

# Temporary input to the script. pend remove.
input_str = "Life is a box of"
# Load environment variables from .env file
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
API_URL = os.getenv("API_URL")

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    """Sends a POST request to provided API_URL and returns the response
    in JSON dict format, enclosed in square brackets.

    Args:
        payload (dict): inputs and other parameters to be submitted to API
        Example:
        {
        "inputs": input_str,
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
    # Testing API response, pend remove.
    print(response.json())
    return response.json()

data = query(
    {
        "inputs": input_str,
        "max_new_tokens":50,
        "num_return_sequences":1,
        "temperature":0.1
        }
    )

generated_text = data[0]['generated_text']

final_output = f"Input: {input_str}\nGenerated Text: {generated_text}"

print(final_output)