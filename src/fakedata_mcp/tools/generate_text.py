"""Generate placeholder text: lorem ipsum paragraphs, realistic sentences, or random words."""

import json

from fakedata_mcp.services.generate_text_service import GenerateText


def generate_text(type: str = "lorem", count: int = 3) -> str:
    """Generate placeholder text: lorem ipsum paragraphs, realistic sentences, or random words

    Returns:
        Generated text string
    """
    service = GenerateText()
    result = service.execute(type=type, count=count)
    return json.dumps(result, indent=2)
