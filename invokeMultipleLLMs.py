import streamlit as st
from litellm import completion
import torch

# --- Streamlit app setup ---
st.title("Multi-LLM Prompting with GPU Support")

# Display GPU info in sidebar
st.sidebar.title("System Info")
st.sidebar.write("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    st.sidebar.write("GPU name:", torch.cuda.get_device_name(0))
else:
    st.sidebar.write("GPU not detected. Using CPU.")

# create a text input for user messages
user_input = st.text_input("Prompt:")

if st.button("Send"):
    if user_input:
        messages = [{"role": "user", "content": user_input}]

        # columns for side-by-side display
        col1, col2 = st.columns(2)

        # llama3
        with col1:
            st.subheader("llama3")
            try:
                response = completion(
                    model="ollama/llama3",
                    messages=messages,
                    device="cuda" if torch.cuda.is_available() else "cpu"
                )
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {str(e)}")

        # gemma 2:2b
        with col2:
            st.subheader("gemma2:2b")
            try:
                response = completion(
                    model="ollama/gemma2:2b",
                    messages=messages,
                    device="cuda" if torch.cuda.is_available() else "cpu"
                )
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {str(e)}")

        st.divider()

        st.write(
            "Exercise for later: install two more models from https://ollama.com/library "
            "[including if you like, https://ollama.com/library/llama2-chinese!], "
            "add two more columns above, send your prompt to FOUR LLMs, and display their responses."
        )

        st.divider()
    else:
        st.warning("Please enter a prompt.")

# --- Sidebar info ---
st.sidebar.title("About")
st.sidebar.write(
    "This app, derived from https://github.com/Shubhamsaboo/awesome-llm-apps, "
    "shows how to invoke (multiple) LLMs via LiteLLM [https://docs.litellm.ai/] - FUN!"
)
st.sidebar.write("Aim: create an ER diagram using AI models")
