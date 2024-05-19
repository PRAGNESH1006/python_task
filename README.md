# Python Task: Fetching and Displaying Citations from an API

This project is designed to fetch data from a paginated API, process the response to identify relevant sources for each response text, and display the results using a user-friendly web interface built with Streamlit.

## Introduction

The goal of this project is to:
1. Fetch data from a paginated API.
2. Identify whether the response for each response-sources pair came from any of the sources.
3. List the sources from which the response was formed (citations).
4. Return the citations for all objects coming from the API.
5. Present the solution through a user-friendly UI using Streamlit.

## Requirements

- Python 3.7 or higher
- The following Python packages:
  - `requests`
  - `nltk`
  - `streamlit`
