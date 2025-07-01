---

# AI Document Summarizer & Key Point Extractor

**Tech Stack:** Python, LangChain, OpenAI (GPT), Streamlit

> *"Turn 50-page contracts and reports into a one-page summary with critical terms extracted. Save hours of manual review."*

---

## What This Tool Does

* Summarizes lengthy PDF documents in seconds
* Extracts key terms like dates, penalties, clauses
* Highlights risky legal or financial language
* Allows custom keywords to focus on
* Outputs clean, readable summaries for review

---

## Features

**1. Instant Summary**
Upload a PDF, click summarize, and get a clean summary with critical points extracted.

**2. Highlights Risky Language**
Terms like "terminate", "liable", or "penalty" are bolded to catch attention during legal or contract reviews.

**3. Batch-Friendly**
Although this demo is single-file, the logic supports batch processing of multiple PDFs.

**4. Customizable**
The core logic can be tweaked to focus on user-specified keywords, sectors (e.g., real estate, finance), or document formats.

---

## Demo Example

**Input File**
`examples/contract_input.png`

**Output Summary**
`examples/summary_output.png`

| Input (Contract Page)                 | Output (Summarized Result)              |
| ------------------------------------- | --------------------------------------- |
| ![Input](examples/contract_input.png) | ![Summary](examples/summary_output.png) |

---

## Folder Structure

```bash
doc-summarizer/
├── app.py                     # Streamlit UI
├── summarize.py               # Summarization + Risk Highlighter
├── utils/
│   └── pdf_to_text.py         # PDF text extraction logic
├── examples/
│   ├── contract_input.png     # Sample input
│   └── summary_output.png     # Sample summary
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview
```

---

## Quickstart

```bash
git clone https://github.com/yourusername/doc-summarizer
cd doc-summarizer
pip install -r requirements.txt
streamlit run app.py
```

---

## Use Cases

* Law firms: auto-review contracts for risky clauses
* Finance teams: summarize loan or investment agreements
* Researchers: condense academic papers
* Corporations: convert meeting notes into executive summaries

---

## Customization

Need this integrated into a legal portal, CRM, or enterprise system?

* Can connect to Dropbox, Google Drive, SharePoint
* Can output CSV, Markdown, or custom formats
* Can be trained on internal documents for better accuracy

---

## Contact

This is a client-facing demo built for Upwork proposals and freelance gigs.
If you'd like a tailored version with your document samples or workflow in mind, feel free to reach out.

---


