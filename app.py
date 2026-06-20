"""
Customer Service AI — Northstar Outfitters
A small Streamlit app that answers customer support questions using the
Claude API, grounded in a local knowledge base.
"""

import os

import streamlit as st
from anthropic import Anthropic, APIError
from dotenv import load_dotenv

from prompts.system_prompt import build_system_prompt
from utils.kb_loader import load_knowledge_base

load_dotenv()

# Using Claude Sonnet 4.6 as the default model. For a high-volume, low-cost
# deployment you could switch this to "claude-haiku-4-5" instead.
MODEL_NAME = "claude-sonnet-4-6"

# Simple guard against extremely long input — generous enough for any real
# support question, but prevents accidental huge pastes from ballooning cost.
MAX_QUESTION_LENGTH = 2000

EXAMPLE_QUESTIONS = [
    "How long does standard shipping take?",
    "Can I return a jacket I bought 40 days ago?",
    "My headlamp won't turn on, what should I check?",
    "I never received my order, what now?",
    "Do you offer price matching?",
]


def get_client() -> Anthropic | None:
    """Create an Anthropic client from the API key in the environment.
    Returns None if the key is missing so the UI can show a friendly error."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return None
    return Anthropic(api_key=api_key)


def ask_claude(client: Anthropic, question: str, category: str) -> str:
    """Send a question to Claude, grounded in the relevant knowledge base
    content for the selected category, and return the plain text reply."""
    kb_text = load_knowledge_base(category)
    system_prompt = build_system_prompt(kb_text)

    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=512,
        system=system_prompt,
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

with st.expander("Need an idea? Try an example question"):
    for example in EXAMPLE_QUESTIONS:
        if st.button(example, key=example):
            st.session_state["question_input"] = example

category = st.selectbox(
    "Support category (optional)",
    ["General", "Shipping", "Returns", "Warranty", "Orders", "Troubleshooting"],
)

question = st.text_area(
    "Your question",
    key="question_input",
    placeholder="e.g. How long does standard shipping take?",
)

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
    elif len(question) > MAX_QUESTION_LENGTH:
        st.warning(
            f"That question is a bit long ({len(question)} characters). "
            f"Please shorten it to under {MAX_QUESTION_LENGTH} characters and try again."
        )
    else:
        with st.spinner("Thinking..."):
            try:
                answer = ask_claude(client, question, category)
                st.write(answer)
            except APIError as e:
                st.error(f"Something went wrong talking to Claude: {e}")
