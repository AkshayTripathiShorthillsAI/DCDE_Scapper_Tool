import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables
load_dotenv()

def process_feature_text(long_text):
    print("Akshay")
    # Define the prompt
    prompt = f'''Return the features of vehicle.It may include the following details:

Engine Performance: Details about the engine type, horsepower, torque, and fuel efficiency.
Transmission: Information on the type of transmission (automatic, manual, CVT) and its features.
Interior Features: Descriptions of comfort features like seating materials, infotainment systems, climate control, and cabin space.
Safety Features: Information on safety systems such as airbags, anti-lock brakes, stability control, and driver-assistance technologies.
Exterior Features: Details about exterior design elements, lighting, wheel size, and paint options.
Technology: Features related to connectivity, navigation systems, and advanced driver-assistance systems (ADAS).
Convenience: Features that enhance user convenience like keyless entry, power windows, and adjustable mirrors.
Cargo Capacity: Information on the space available for cargo and storage solutions.
Fuel Efficiency: Data on the vehicle’s fuel economy and emissions.
Warranty and Maintenance: Information about the warranty coverage and maintenance packages.

long text:{long_text}
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
