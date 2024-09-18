import json
import streamlit as st

def store_results_in_json(answers):
    result_json = {"answers": answers}
    with open("results.json", "w", encoding="utf-8") as file:
        json.dump(result_json, file, indent=4)
    st.success("Results stored in 'results.json'.")
