# Project Rules for AI Coding Assistant

These rules apply to any AI coding assistant (including Claude) helping build the `customer-service-ai` project. Follow them consistently throughout development.

## Code Style and Simplicity

- Keep code beginner-friendly. Prefer clarity over cleverness.
- Prefer simple Python and Streamlit. Avoid unnecessary abstraction layers.
- Do not add unnecessary frameworks or libraries (no LangChain, no ORMs, etc.) unless explicitly requested.
- Keep files small and understandable. Split logic into clear, single-purpose files rather than one giant script.

## Architecture Boundaries

- Do not add databases or authentication during the MVP phase.
- Do not introduce Docker, deployment configs, or vector databases unless explicitly requested.
- Preserve the existing project structure. Do not reorganize folders/files without asking first.
- Ask before making major architecture changes (e.g., switching frameworks, adding new core dependencies).

## Process and Communication

- Make one feature at a time. Do not implement multiple phases at once unless asked.
- Do not rewrite the entire project without asking first.
- Explain changes clearly: what was changed, why, and what files were affected.
- When uncertain about a requirement, ask a clarifying question instead of guessing.

## Security

- Do not expose API keys in code, logs, commit history, or example files.
- Always read the API key from environment variables via `python-dotenv`.
- Remind the user to add `.env` to `.gitignore` if it is ever missing.

## AI Behavior in the App Itself

- The assistant logic must stay grounded in the knowledge base — do not write prompts or code that encourage the model to invent policies.
- Escalation logic should be simple and rule-based or prompt-based, not over-engineered.

## Documentation

- Keep documentation files (`README.md`, `SPEC.md`, etc.) up to date when functionality changes.
- Use plain, professional language in all docs — avoid hype or overly technical jargon.
