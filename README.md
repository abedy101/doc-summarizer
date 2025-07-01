
---

````markdown
# AI Document Summarizer & Key Term Extractor

A powerful, client-ready tool that summarizes long documents and extracts key terms in seconds. Designed for legal teams, researchers, and corporate clients who need to review large files fast.

This app uses OpenAI’s GPT models and LangChain to turn complex contracts, reports, or research papers into short, structured summaries with highlights of risky or critical language.

---

## What This Tool Does

- Accepts PDF or text documents  
- Extracts bullet-point summaries  
- Flags high-risk terms (e.g., "termination", "indemnify", "liable")  
- Exports structured output (copyable, downloadable)  
- Optional: Batch summarization for multiple files

---

## Key Features

### 1. Smart Summarization  
Automatically generates a short summary of the most important points in your document.

### 2. Risk Flagging  
Terms like *"terminate"*, *"indemnify"*, or *"noncompliance"* are highlighted in bold for fast review.

### 3. Upload-and-Go  
Built with Streamlit. No coding or installation knowledge required. Upload your PDF and get your summary in seconds.

### 4. Extensible  
Easily adjust what terms are flagged, or customize the summary format (markdown, CSV, etc.)

---

## Demo Screenshot

**Input:** `examples/sample-contract.pdf`  
**Output Summary:**  
- Agreement between Santa Cruz County and Consultant  
- Consultant provides services listed in Scope of Work  
- Named key personnel required to remain consistent  
- Progress reports submitted monthly  
- Payments based on approved milestones  
- Risk terms: **terminate**, **indemnify**, **reimbursed**

| Input PDF | Output Summary |
|-----------|----------------|
| ![Input](examples/sample-contract.png) | ![Summary](examples/sample-summary.png) |

---

## How to Use

```bash
git clone https://github.com/abedy101/doc-summarizer
cd doc-summarizer
pip install -r requirements.txt
````

Then run:

```bash
streamlit run app.py
```

Upload a document and get instant summaries and flagged clauses in the browser.

---

## Folder Structure

```bash
doc-summarizer/
├── examples/          # Sample input PDFs and output screenshots
├── utils/             # PDF-to-text preprocessing logic
├── summarize.py       # Core summarization + flagging logic
├── app.py             # Streamlit UI
├── requirements.txt   # Python dependencies
└── README.md          # You are here
```

---

## Use Cases

* Law firms summarizing contracts and terms
* Researchers reviewing academic papers
* Teams cleaning up meeting notes and long reports
* Procurement teams screening vendor proposals

---

## Customization

This project can be extended to:

* Accept DOCX or email input formats
* Customize risk terms and thresholds
* Run batch summarization on folders
* Integrate into enterprise workflows (APIs, databases)

---

## Need Help?

This is a demo version. If you want a custom solution:

* I can train it on your documents
* Add multi-language support
* Deploy securely on your infrastructure

Get in touch via GitHub or Upwork for consultation.

```

---


