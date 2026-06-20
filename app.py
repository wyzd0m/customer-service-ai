"""
Customer Service AI — Northstar Outfitters
A small Streamlit app that answers customer support questions using the
Claude API, grounded in a local knowledge base.

Phase 2: basic UI skeleton only. Claude API wiring is added in later phases.
"""

import os

import streamlit as st
from anthropic import Anthropic, APIError
from dotenv import load_dotenv

load_dotenv()

# Using Claude Sonnet 4.6 as the default model. For a high-volume, low-cost
# deployment you could switch this to "claude-haiku-4-5" instead.
MODEL_NAME = "claude-sonnet-4-6"


def get_client() -> Anthropic | None:
    """Create an Anthropic client from the API key in the environment.
    Returns None if the key is missing so the UI can show a friendly error."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return None
    return Anthropic(api_key=api_key)


def ask_claude(client: Anthropic, question: str) -> str:
    """Send a question to Claude and return the plain text reply.
    This is a minimal test call for Phase 3 — knowledge base grounding
    and the real system prompt are added in later phases."""
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=512,
        messages=[{"role": "user", "content": question}],
    )
    return response.content[0].text


st.set_page_config(page_title="Northstar Outfitters Support", page_icon="🏔️")

st.title("🏔️ Northstar Outfitters — Customer Support Assistant")
st.write(
    "Ask a question about shipping, returns, warranty, orders, or product "
    "troubleshooting for Northstar Outfitters (a fictional outdoor gear company). "
    "This assistant only answers from a small built-in knowledge base — it will "
    "tell you when something needs a human agent instead of guessing."
)

category = st.selectbox(
    "Support category (optional)",
    ["General", "Shipping", "Returns", "Warranty", "Orders", "Troubleshooting"],
)

question = st.text_area("Your question", placeholder="e.g. How long does standard shipping take?")

submitted = st.button("Get Answer")

if submitted:
    client = get_client()
    if client is None:
        st.error(
            "No Anthropic API key found. Add ANTHROPIC_API_KEY to your .env file "
            "(see .env.example) and restart the app."
        )
    elif not question.strip():
        st.warning("Please enter a question before submitting.")
    else:
        with st.spinner("Thinking..."):
            try:
                answer = ask_claude(client, question)
                st.write(answer)
            except APIError as e:
                st.error(f"Something went wrong talking to Claude: {e}")
