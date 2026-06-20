"""
Loads the local knowledge base (Markdown files) into a single string that
gets inserted into the system prompt.

Kept intentionally simple for the MVP: just read every .md file in
knowledge_base/ and concatenate them with clear section headers. No
database, no embeddings, no vector search.
"""

from pathlib import Path

KNOWLEDGE_BASE_DIR = Path(__file__).resolve().parent.parent / "knowledge_base"

# Maps the category shown in the UI dropdown to the knowledge base file(s)
# that are most relevant to it. "General" loads everything.
CATEGORY_FILES = {
    "Shipping": ["shipping.md"],
    "Returns": ["returns.md"],
    "Warranty": ["warranty.md"],
    "Orders": ["orders.md"],
    "Troubleshooting": ["troubleshooting.md"],
}


def load_knowledge_base(category: str = "General") -> str:
    """Return the combined text of relevant knowledge base files.

    For a specific category, load that category's file plus the escalation
    rules (always needed so the assistant knows when to hand off). For
    "General" (or anything unrecognized), load everything so the assistant
    has full context.
    """
    if category in CATEGORY_FILES:
        filenames = CATEGORY_FILES[category] + ["escalation_rules.md"]
    else:
        filenames = sorted(p.name for p in KNOWLEDGE_BASE_DIR.glob("*.md"))

    sections = []
    for filename in filenames:
        file_path = KNOWLEDGE_BASE_DIR / filename
        if file_path.exists():
            sections.append(f"--- {filename} ---\n{file_path.read_text()}")

    return "\n\n".join(sections)
