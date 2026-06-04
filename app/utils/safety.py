PROMPT_INJECTION_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "system prompt",
    "reveal your instructions",
    "bypass security",
    "developer message",
]


def detect_prompt_injection(
    text: str
) -> bool:

    text = text.lower()

    for pattern in (
        PROMPT_INJECTION_PATTERNS
    ):

        if pattern in text:
            return True

    return False