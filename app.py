# hf_api_app.py
import streamlit as st
import requests

API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("🤖 Text Generation via Hugging Face API")
text_input = st.text_area("Prompt")

if st.button("Generate"):
    output = query({"inputs": text_input})
    if isinstance(output, dict) and output.get("error"):
        st.error(output["error"])
    else:
        st.success(output[0]['generated_text'])
