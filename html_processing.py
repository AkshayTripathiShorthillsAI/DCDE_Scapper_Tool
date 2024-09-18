import requests
import html2text
from bs4 import BeautifulSoup

# Fetch HTML content from a product URL
def fetch_html(product_url):
    try:
        response = requests.get(product_url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        return f"Error fetching HTML: {e}"

# Convert HTML content to plain text
def convert_html_to_plain_text(html_content):
    h = html2text.HTML2Text()
    h.ignore_links = True
    return h.handle(html_content)

# Additional function to clean the HTML (optional)
def clean_html(html_content):
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True  # Optionally ignore images
    cleaned_text = h.handle(html_content)
    return ' '.join(cleaned_text.split())  # Clean up spaces
