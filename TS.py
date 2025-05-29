import streamlit as st

# Set page config FIRST, before any other Streamlit commands
st.set_page_config(page_title="Text Summarizer", layout="centered")

import os
os.environ["TRANSFORMERS_NO_TF"] = "1"  # Prevent TensorFlow import

from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

st.title("📝 Text Summarizer with Transformers")

text = st.text_area("Paste your text here:", height=250)

max_len = st.slider("Maximum Summary Length", 30, 300, 100)
min_len = st.slider("Minimum Summary Length", 10, 100, 30)

if st.button("Summarize"):
    if text.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
            st.success("✅ Summary Generated!")
            st.text_area("Summary", summary[0]['summary_text'], height=150)
