# Text Summarizer App (Hugging Face BART + Streamlit)

## 📌 Overview
This project is an interactive web application that summarizes long text into concise summaries using **Hugging Face Transformers**. The app is built with **Streamlit** and leverages the **BART large CNN model** for abstractive summarization.

## 🛠️ Technologies Used
- Python  
- Hugging Face Transformers  
- Streamlit  

## ⚙️ Methodology
1. Integrated Hugging Face `pipeline` for summarization.  
2. Used **facebook/bart-large-cnn** model for abstractive text summarization.  
3. Built a Streamlit UI for user interaction:
   - Text input area  
   - Adjustable minimum/maximum summary length sliders  
   - Generate summary with one click  
4. Optimized with caching (`st.cache_resource`) for faster model loading.  

## 📊 Features
- Summarizes text of any length.  
- Adjustable summary size (min/max length).  
- Instant user feedback with Streamlit widgets.  

## 🚀 How to Run
1. Clone the repo:  
```bash
git clone <repo-link>
cd text-summarizer-app
