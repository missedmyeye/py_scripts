"""The purpose of this script is to generate text from a LLM with a given text.

Returns:
    generated_text (str): continuated text 
"""
import os
import json
import sys
from dotenv import load_dotenv
import requests

def query(api_url,payload):
    """Sends a POST request to provided API_URL and returns the response
    in JSON dict format, enclosed in square brackets.

    Args:
        api_url (str): URL to inference API
        payload (dict): inputs and other parameters to be submitted to API
        Example:
        {
        "inputs": "Life is a box of",
        "max_new_tokens":50,
        "num_return_sequences":1,
        "temperature":0.8
        }

    Returns:
        response.json(): response from API
        Example:
        [{'generated_text': 'Life is a box of cards that you may find interesting, 
        or some random action on the box that you may be able to take to make a 
        character. Once a character is learned, they become a part of your 
        story for a few days. They'}]

    """
    # Load environment variables from .env file
    load_dotenv()

    api_token = os.getenv("API_TOKEN")

    headers = {"Authorization": f"Bearer {api_token}"}

    response = requests.post(api_url, headers=headers, json=payload)

    return response.json()

def gen_text(api_url,input_str,max_new_tokens=50,num_return_sequences=1,temperature=0.8):
    """Organizes input data and config parameters to send to the specified inference API.

    Args:
        api_url (str): URL to inference API
        input_str (str): Input text for continuated generation
        max_new_tokens (int, optional): The amount of new tokens to be generated. Defaults to 50.
        num_return_sequences (int, optional): The number of proposition you want to be returned. 
            Defaults to 1.
        temperature (float, optional): The temperature of the sampling operation. Defaults to 0.8.

    Returns:
        _type_: _description_
    """
    data = query(api_url,
        {
            "inputs": input_str,
            "max_new_tokens":max_new_tokens,
            "num_return_sequences":num_return_sequences,
            "temperature":temperature
            }
        )

    generated_text = data[0]['generated_text']

    return generated_text

if __name__ == "__main__":
    # Read configuration parameters from the file
    config = {}
    with open("gen_config.json", 'r') as file:
        config = json.load(file)[0]

    API_URL = config.get("API_URL")

    # Read input from command-line argument, default to config value if no input
    if len(sys.argv) > 1 and sys.argv[1].strip():
        INPUT_STR = sys.argv[1]
    else:
        INPUT_STR = config.get("input")

    # Assigning remaining parameters from config
    max_new_tokens = config.get("max_new_tokens")
    num_return_sequence = config.get("num_return_sequences")
    temperature = config.get("temperature")

    generated_text = gen_text(API_URL,INPUT_STR,max_new_tokens,num_return_sequence,temperature)
    final_output = f"Input: {INPUT_STR}\nGenerated Text: {generated_text}"

    print(final_output)
