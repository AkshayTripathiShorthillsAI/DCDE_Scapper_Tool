# process_data.py

import os
from dotenv import load_dotenv
import requests
import json
from prompts import GENERAL_PROMPT, FEATURES_PROMPT, DIMENSION_PROMPT, OPERATIONS_PROMPT

# Load environment variables
load_dotenv()

def get_prompt(prompt_type):
    """
    Retrieve the prompt based on the prompt type.

    Args:
        prompt_type (str): Type of prompt to retrieve ('general' or 'features').

    Returns:
        str: The selected prompt.
    """
    if prompt_type == 'general':
        return GENERAL_PROMPT
    elif prompt_type == 'features':
        return FEATURES_PROMPT
    elif prompt_type == 'dimensions':
        return DIMENSION_PROMPT
    elif prompt_type == 'operations':
        return OPERATIONS_PROMPT
    else:
        raise ValueError("Invalid prompt type. Choose 'general' or 'features'.")

def process_data(long_text, prompt_type):
    """
    Process the data based on the prompt type.

    Args:
        long_text (str): The text to be processed.
        prompt_type (str): Type of prompt to use ('general' or 'features').

    Returns:
        str: The processed result from the API.
    """
    prompt = get_prompt(prompt_type).format(long_text=long_text)

    # Define the headers and API URL
    api_url = os.getenv("Llama_API_URL")  # Load Llama 3 API URL from .env
    api_key = os.getenv("Llama_API_KEY")  # Load Llama 3 API key from .env

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    payload = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "temperature": 0.7,
        "top_p": 0.95,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 2048
    }

    # Make the POST request to Llama 3 API
    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Check if the request was successful
        
        response_json = response.json()
        generated_text = response_json['choices'][0]['message']['content']
        return generated_text

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except KeyError as e:
        print(f"Key error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    long_text = "Your long text goes here."
    prompt_type = 'general'  # Change to 'features' if needed

    try:
        result = process_data(long_text, prompt_type)
        if result:
            print("Processed Result:")
            print(result)
    except ValueError as e:
        print(e)
