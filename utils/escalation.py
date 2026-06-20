"""
Simple, rule-based escalation detection.

The system prompt instructs Claude to prefix any reply that needs a human
agent with the ESCALATION_MARKER text. This module just checks for that
marker and splits it from the rest of the message — no extra API calls,
no classifier, nothing fancy. Beginner-friendly by design.
"""

from dataclasses import dataclass

from prompts.system_prompt import ESCALATION_MARKER


@dataclass
class ParsedResponse:
    text: str
    is_escalation: bool


def parse_response(raw_response: str) -> ParsedResponse:
    """Check whether Claude's reply is an escalation and clean up the text."""
    stripped = raw_response.strip()
    if stripped.startswith(ESCALATION_MARKER):
        message = stripped[len(ESCALATION_MARKER):].strip()
        return ParsedResponse(text=message, is_escalation=True)
    return ParsedResponse(text=stripped, is_escalation=False)
