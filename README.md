# AI Document Summarizer

A lightweight, no-login app that extracts key insights from PDF documents using GPT and highlights risky contract terms for quick review. Built with Streamlit and LangChain.

---

## Key Features

### 1. Smart Summarization  
Generates a concise summary of the most important information in your uploaded document.

### 2. Risk Flagging  
Highlights sensitive or risky terms like `terminate`, `indemnify`, or `noncompliance` in **bold** for faster scanning.

### 3. Upload-and-Go  
Just upload your PDF — no coding or config required. Summaries are generated instantly in your browser.

### 4. Extensible  
Customize risk keywords, tweak the summary format (Markdown, CSV, etc.), or plug in your own prompt templates.

---

## Demo Screenshot

**Input PDF:** [`examples/sample-contract.pdf`](examples/sample-contract.pdf)  
**Output Summary:**

- Agreement between Santa Cruz County and Consultant  
- Consultant provides services listed in Scope of Work  
- Named key personnel must remain unchanged without consent  
- Progress reports submitted monthly  
- Payments based on approved milestones  

Risk terms highlighted in bold for quick review.

---

## How to Run Locally

```bash
git clone https://github.com/abedy101/doc-summarizer.git
cd doc-summarizer
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
streamlit run app.py

