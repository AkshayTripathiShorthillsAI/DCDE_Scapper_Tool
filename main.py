import streamlit as st
import asyncio
from html_processing import fetch_html, convert_html_to_plain_text, clean_html
from general import process_text
from features import process_feature_text
from operations import process_operation_text
from dimensions import process_dimension_text

def main():
    st.title("Product Information Extractor")

    # Initialize session state variables to store intermediate results
    if "html_content" not in st.session_state:
        st.session_state.html_content = ""
    if "plain_text_content" not in st.session_state:
        st.session_state.plain_text_content = ""
    if "extracted_general_details" not in st.session_state:
        st.session_state.extracted_general_details = ""
    if "extracted_feature_details" not in st.session_state:
        st.session_state.extracted_feature_details = ""
    if "extracted_operation_details" not in st.session_state:
        st.session_state.extracted_operation_details = ""
    if "extracted_dimension_details" not in st.session_state:
        st.session_state.extracted_dimension_details = ""


    # Input URL
    product_url = st.text_input("Enter Product URL:", "https://www.crown.com/en-us/forklifts/stackers/m-intermediate-stacker.html")

    # Button to Fetch HTML
    if st.button("Fetch HTML Content"):
        try:
            st.session_state.html_content = asyncio.run(fetch_html(product_url))
        except RuntimeError:
            st.error("Error fetching HTML content. Please try again.")

    # Show HTML content if fetched
    if st.session_state.html_content:
        st.subheader("HTML Content")
        st.text_area("HTML Content", value=st.session_state.html_content, height=300, key="html_content_area")

    # Button to Convert HTML to Plain Text
    if st.session_state.html_content and st.button("Convert to Plain Text"):
        st.session_state.plain_text_content = clean_html(st.session_state.html_content)

    # Show plain text content if already converted
    if st.session_state.plain_text_content:
        st.subheader("Plain Text Content")
        st.text_area("Plain Text Content", value=st.session_state.plain_text_content, height=300, key="plain_text_area")

    # Button to Process Plain Text with General
    if st.session_state.plain_text_content and st.button("Extract Details"):
        st.session_state.extracted_general_details = process_text(st.session_state.plain_text_content)

    # Show extracted details if already processed
    if st.session_state.extracted_general_details:
        st.subheader("Extracted General Details")
        st.text_area("Extracted General Details", value=st.session_state.extracted_general_details, height=300, key="extracted_general_details_area")
    
    # Button to Process Plain Text with Features
    if st.session_state.plain_text_content and st.button("Extract Features"):
        st.session_state.extracted_feature_details = process_feature_text(st.session_state.plain_text_content)

    # Show extracted details if already processed
    if st.session_state.extracted_feature_details:
        st.subheader("Extracted Feature Details")
        st.text_area("Extracted Feature Details", value=st.session_state.extracted_feature_details, height=300, key="extracted_feature_details_area")
    
    # Button to Process Plain Text with Operations
    if st.session_state.plain_text_content and st.button("Extract Operations"):
        st.session_state.extracted_operation_details = process_operation_text(st.session_state.plain_text_content)

    # Show extracted details if already processed
    if st.session_state.extracted_operation_details:
        st.subheader("Extracted Operation Details")
        st.text_area("Extracted Operation Details", value=st.session_state.extracted_operation_details, height=300, key="extracted_operation_details_area")
    
    # Button to Process Plain Text with Dimensions
    if st.session_state.plain_text_content and st.button("Extract Dimensions"):
        st.session_state.extracted_dimension_details = process_dimension_text(st.session_state.plain_text_content)

    # Show extracted details if already processed
    if st.session_state.extracted_dimension_details:
        st.subheader("Extracted Dimension Details")
        st.text_area("Extracted Dimension Details", value=st.session_state.extracted_dimension_details, height=300, key="extracted_dimension_details_area")

    # Display the entered product URL
    st.subheader("Product URI")
    st.text(f"Product URL: {product_url}")

if __name__ == "__main__":
    main()
