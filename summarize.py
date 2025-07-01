from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Function to highlight risky terms in the text
def highlight_risky_text(text):
    risky_terms = ["indemnify", "liable", "terminate", "breach", "penalty", "litigation", "damages"]
    for term in risky_terms:
        text = text.replace(term, f"**{term.upper()}**")
    return text

# Summarize the input text using GPT
def summarize_text(text, temperature=0.3):
    # Convert raw text to a Document object for LangChain
    doc = Document(page_content=text)

    # Set up the OpenAI Chat model
    llm = ChatOpenAI(
        temperature=temperature,
        model_name="gpt-3.5-turbo"
    )

    # Define the summary prompt
    prompt_template = """Summarize the following document into clear, concise bullet points.
Include key obligations, penalties, and deadlines where possible.

"{text}"
"""
    prompt = PromptTemplate.from_template(prompt_template)

    # Load summarize chain
    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)

    # Run the summarizer
    summary = chain.run([doc])
    return summary
