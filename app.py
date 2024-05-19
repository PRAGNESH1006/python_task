import requests
import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from collections import defaultdict

# Ensure you have the necessary NLTK resources
nltk.download('punkt')

# Function to fetch data from the API
def fetch_data(api_url):
    data = []
    page = 1
    while True:
        response = requests.get(f"{api_url}?page={page}")
        if response.status_code != 200:
            st.error("Failed to fetch data from the API.")
            break
        try:
            page_data = response.json()
            st.write(f"Raw API response for page {page}:")
            st.json(page_data)  # Display the raw API response for debugging
            if not isinstance(page_data, list):
                st.error("Unexpected API response format.")
                break
            if not page_data:
                break
            data.extend(page_data)
        except ValueError as e:
            st.error(f"Error parsing JSON: {e}")
            break
        page += 1
    return data

# Function to identify citations
def identify_citations(data):
    citations = defaultdict(list)
    for item in data:
        if isinstance(item, dict):
            response_text = item.get('response', '')
            sources = item.get('sources', [])
            for source in sources:
                if isinstance(source, dict):
                    source_context = source.get('context', '')
                    if source_context in response_text:
                        citations[response_text].append(source)
        else:
            st.warning(f"Unexpected item type: {type(item)}, value: {item}")
    return citations

# Main function
def main():
    st.title("Response Citations")

    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    data = fetch_data(api_url)

    # Debug: Print a sample of the data
    if data:
        st.write("Sample data from API:", data[:2])  # Print first 2 items for inspection

        citations = identify_citations(data)

        for response, sources in citations.items():
            st.subheader("Response")
            st.write(response)
            st.subheader("Citations")
            if sources:
                for source in sources:
                    st.write(f"ID: {source['id']}, Context: {source['context']}, Link: {source.get('link', 'N/A')}")
            else:
                st.write("No citations found")

if __name__ == "__main__":
    main()
