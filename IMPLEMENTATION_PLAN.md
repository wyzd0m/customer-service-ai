# Implementation Plan: Customer Service AI

A step-by-step build plan broken into phases. Each phase lists the specific files to create or edit. Complete phases in order; do not skip ahead.

## Phase 1: Project Setup

- Create project folder `customer-service-ai/`
- Create `requirements.txt` (streamlit, anthropic, python-dotenv)
- Create `.env.example`
- Create `.gitignore` (include `.env`, `venv/`, `__pycache__/`)
- Initialize git repository

**Files:** `requirements.txt`, `.env.example`, `.gitignore`

## Phase 2: Basic Streamlit UI

- Create `app.py` with a simple title, description, and text input box
- Add a placeholder "Submit" button with no real logic yet
- Confirm the app runs locally with `streamlit run app.py`

**Files:** `app.py`

## Phase 3: Claude API Connection

- Load API key from `.env` using `python-dotenv`
- Add a simple function to call the Claude API with a test prompt
- Confirm a basic response displays in the Streamlit UI

**Files:** `app.py`, `.env`

## Phase 4: Prompt Design

- Create `prompts/system_prompt.py`
- Write a system prompt instructing Claude to:
  - Act as a Northstar Outfitters support assistant
  - Answer only from provided knowledge base content
  - Say "I don't know, please contact a human agent" when unsure
  - Stay professional, friendly, and concise

**Files:** `prompts/system_prompt.py`

## Phase 5: Local Knowledge Base

- Create `knowledge_base/` folder
- Add individual Markdown files: `shipping.md`, `returns.md`, `warranty.md`, `orders.md`, `troubleshooting.md`, `escalation_rules.md`
- Create `utils/kb_loader.py` to load and combine knowledge base content

**Files:** `knowledge_base/*.md`, `utils/kb_loader.py`

## Phase 6: Customer Support Answer Generation

- Connect the knowledge base content to the prompt sent to Claude
- Update `app.py` to pass the user's question + relevant KB content to Claude
- Display the generated answer in the UI

**Files:** `app.py`, `utils/kb_loader.py`, `prompts/system_prompt.py`

## Phase 7: Escalation Detection

- Create `utils/escalation.py` with simple logic/prompt instructions for detecting when escalation is needed
- Update the UI to clearly flag escalated responses (e.g., a warning box)

**Files:** `utils/escalation.py`, `app.py`

## Phase 8: Testing with Sample Questions

- Manually test using the question list in `TESTING.md`
- Verify grounded answers, correct escalations, and graceful error handling
- Fix any issues found

**Files:** `app.py`, `utils/kb_loader.py`, `utils/escalation.py`

## Phase 9: README Polish and GitHub Cleanup

- Update `README.md` with final screenshots/details if desired
- Confirm `.env` is not committed
- Clean up unused code and comments
- Add `LICENSE` file

**Files:** `README.md`, `LICENSE`

## Phase 10: Future Upgrades (Not Part of MVP)

- Plan for RAG/vector search, conversation history, admin KB editor, etc.
- Document these in `FEATURES.md` under "Future Advanced Features"

**Files:** `FEATURES.md`
