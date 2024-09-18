import asyncio
import html2text
from langchain_community.document_loaders import AsyncChromiumLoader

# Fetch HTML content from a product URL asynchronously
async def fetch_html(product_url):
    loader = AsyncChromiumLoader([product_url])
    html_documents = await loader.aload()
    return html_documents[0].page_content if html_documents else None

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
