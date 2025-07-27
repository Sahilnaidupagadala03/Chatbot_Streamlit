import streamlit as st
import requests

# App title
st.title("🤖 Hugging Face Chatbot")

# Predefined list of models
model_options = {
    "LLaMA 2B (meta-llama/Llama-2-7b-chat-hf)": "meta-llama/Llama-2-7b-chat-hf",
    "Falcon (tiiuae/falcon-7b-instruct)": "tiiuae/falcon-7b-instruct",
    "Mistral (mistralai/Mistral-7B-Instruct-v0.1)": "mistralai/Mistral-7B-Instruct-v0.1",
    "GPT-J (EleutherAI/gpt-j-6B)": "EleutherAI/gpt-j-6B",
    "BLOOM (bigscience/bloom)": "bigscience/bloom",
    "DistilGPT2 (distilgpt2)": "distilgpt2"
}

# Model selection
model_name = st.selectbox("Select a Hugging Face Model", list(model_options.keys()))

# User input
user_input = st.text_area("Enter your message", height=150)

# Get API Key from st.secrets
API_URL = f"https://api-inference.huggingface.co/models/{model_options[model_name]}"
headers = {"Authorization": f"Bearer {st.secrets[Key2]}"}

# Function to query model
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        # Some models return list of dicts with 'generated_text', others may differ
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif isinstance(result, dict) and "generated_text" in result:
            return result["generated_text"]
        else:
            return result
    else:
        return f"❌ Error: {response.status_code} - {response.text}"

# Submit button
if st.button("Get Response"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        with st.spinner("Generating response..."):
            output = query({"inputs": user_input})
        st.markdown("### 💬 Response")
        st.write(output)
