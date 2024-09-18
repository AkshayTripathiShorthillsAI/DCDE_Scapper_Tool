import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables
load_dotenv()

def process_operation_text(long_text):
    print("Akshay")
    # Define the prompt
    prompt = f"""You have been given a long text. Your task is to extract specific operational specifications and convert them into a JSON format. For each attribute listed below, provide the "label" and "desc" using the format shown. Ensure that the extracted options are concise and accurately reflects the information provided in the text.

Long text: {long_text}
"""

    # Define the headers and API URL
    api_url = os.getenv("Llama_API_URL")  # Load Llama 3 API URL from .env
    api_key = os.getenv("Llama_API_KEY")  # Load Llama 3 API key from .env

    print(api_url, api_key)
    
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
        print(response)
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
    long_text = "Your long text goes here."
    extracted_details = process_operation_text(long_text)
    if extracted_details:
        print("Extracted Details:")
        print(extracted_details)
