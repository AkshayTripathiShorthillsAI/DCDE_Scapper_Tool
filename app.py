import streamlit as st
import asyncio
from html_processing import fetch_html, clean_html
from process_data import process_data

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
            st.success("HTML content fetched successfully!")
        except RuntimeError:
            st.error("Error fetching HTML content. Please try again.")

    # Show HTML content if fetched
    if st.session_state.html_content:
        st.subheader("HTML Content")
        st.text_area("HTML Content", value=st.session_state.html_content, height=300, key="html_content_area")

    # Button to Convert HTML to Plain Text
    if st.session_state.html_content and st.button("Convert to Plain Text"):
        try:
            st.session_state.plain_text_content = clean_html(st.session_state.html_content)
            st.success("HTML converted to plain text successfully!")
        except Exception as e:
            st.error(f"Error converting HTML to plain text: {e}")

    # Show plain text content if already converted
    if st.session_state.plain_text_content:
        st.subheader("Plain Text Content")
        st.text_area("Plain Text Content", value=st.session_state.plain_text_content, height=300, key="plain_text_area")

    # Button to Process Plain Text with General
    if st.session_state.plain_text_content and st.button("Extract General Details"):
        try:
            st.session_state.extracted_general_details = process_data(st.session_state.plain_text_content, 'general')
            st.success("General details extracted successfully!")
        except Exception as e:
            st.error(f"Error extracting general details: {e}")

    # Show extracted general details if already processed
    if st.session_state.extracted_general_details:
        st.subheader("Extracted General Details")
        st.text_area("Extracted General Details", value=st.session_state.extracted_general_details, height=300, key="extracted_general_details_area")
    
    # Button to Process Plain Text with Features
    if st.session_state.plain_text_content and st.button("Extract Features"):
        try:
            st.session_state.extracted_feature_details = process_data(st.session_state.plain_text_content, 'features')
            st.success("Feature details extracted successfully!")
        except Exception as e:
            st.error(f"Error extracting features: {e}")

    # Show extracted feature details if already processed
    if st.session_state.extracted_feature_details:
        st.subheader("Extracted Feature Details")
        st.text_area("Extracted Feature Details", value=st.session_state.extracted_feature_details, height=300, key="extracted_feature_details_area")
    
    # Button to Process Plain Text with Operations
    if st.session_state.plain_text_content and st.button("Extract Operations"):
        try:
            st.session_state.extracted_operation_details = process_data(st.session_state.plain_text_content, 'operations')
            st.success("Operation details extracted successfully!")
        except Exception as e:
            st.error(f"Error extracting operations: {e}")

    # Show extracted operation details if already processed
    if st.session_state.extracted_operation_details:
        st.subheader("Extracted Operation Details")
        st.text_area("Extracted Operation Details", value=st.session_state.extracted_operation_details, height=300, key="extracted_operation_details_area")
    
    # Button to Process Plain Text with Dimensions
    if st.session_state.plain_text_content and st.button("Extract Dimensions"):
        try:
            st.session_state.extracted_dimension_details = process_data(st.session_state.plain_text_content, 'dimensions')
            st.success("Dimension details extracted successfully!")
        except Exception as e:
            st.error(f"Error extracting dimensions: {e}")

    # Show extracted dimension details if already processed
    if st.session_state.extracted_dimension_details:
        st.subheader("Extracted Dimension Details")
        st.text_area("Extracted Dimension Details", value=st.session_state.extracted_dimension_details, height=300, key="extracted_dimension_details_area")

    # Display the entered product URL
    st.subheader("Product URI")
    st.text(f"Product URL: {product_url}")


    st.markdown("---")
    st.markdown("### Created by AkshayTriapthiShorthillsAI")


if __name__ == "__main__":
    main()
