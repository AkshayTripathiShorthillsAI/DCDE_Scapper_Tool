import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables
load_dotenv()

def process_text(long_text):
    print("Akshay")
    # Define the prompt
    prompt = f'''You are an scrapper for a website. Given a long text, extract and return only json:

Manufacturer: Identify the name of the company or brand that produces the product.

Model: Find the specific model name or number associated with the product.

Year: Determine the manufacturing year or the model year for the product.

MSRP (Manufacturer's Suggested Retail Price): Extract the suggested retail price if mentioned, otherwise indicate if it's not provided.

Category: Identify the general category or type of product (e.g., Forklifts, Lift Trucks).

Subcategory: Find any subcategory or specific type within the general category (e.g., Walkie Straddle Stacker).

Description: Extract a brief description or overview of the product, highlighting its key features and uses.

Countries: List the countries where the product is available or mentioned.

long text:{long_text}

json:
"general": 
      "manufacturer": "",
      "model": "",
      "year": 2024,
      "msrp": 0,
      "category": "",
      "subcategory": "",
      "description": "",
      "countries": ["USA","CA"]
'''

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
    extracted_details = process_text(long_text)
    if extracted_details:
        print("Extracted Details:")
        print(extracted_details)
