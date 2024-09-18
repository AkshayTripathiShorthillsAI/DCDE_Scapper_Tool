
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

def process_text(long_text):
    # Define the prompt
    prompt =f''' Given a long text, extract and return the following details in json format:

Manufacturer: Identify the name of the company or brand that produces the product.

Model: Find the specific model name or number associated with the product.

Year: Determine the manufacturing year or the model year for the product.

MSRP (Manufacturer's Suggested Retail Price): Extract the suggested retail price if mentioned, otherwise indicate if it's not provided.

Category: Identify the general category or type of product (e.g., Forklifts, Lift Trucks).

Subcategory: Find any subcategory or specific type within the general category (e.g., Walkie Straddle Stacker).

Description: Extract a brief description or overview of the product, highlighting its key features and uses.

Countries: List the countries where the product is available or mentioned.


long text:{long_text}

json format:
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

    # Call the Groq API for completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content
