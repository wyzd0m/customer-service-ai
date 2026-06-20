"""
Customer Service AI — Northstar Outfitters
A small Streamlit app that answers customer support questions using the
Claude API, grounded in a local knowledge base.

Phase 2: basic UI skeleton only. Claude API wiring is added in later phases.
"""

import streamlit as st

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
    st.info("Answer generation isn't wired up yet — coming in the next phase.")
