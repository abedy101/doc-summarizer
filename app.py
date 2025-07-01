import streamlit as st
from utils.pdf_to_text import extract_text_from_pdf
from summarize import summarize_text, highlight_risky_text

st.set_page_config(page_title="AI Document Summarizer", layout="wide")
st.title("📄 AI Document Summarizer & Risk Highlighter")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file is not None:
    raw_text = extract_text_from_pdf(uploaded_file)
    
    st.subheader("Original Extracted Text")
    st.text_area("Full text from PDF:", raw_text[:3000], height=200)

    if st.button("Summarize"):
        with st.spinner("Summarizing document..."):
            summary = summarize_text(raw_text)
            summary = highlight_risky_text(summary)

        st.subheader("Summary Output")
        st.markdown(summary)
