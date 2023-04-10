"""
Extract Code Module
-------------------

This module contains the extract_code function, which is responsible for extracting a specific code block
from a given text. The function searches for a code block enclosed by triple backticks (```) and returns
the contents within it.
"""

import re
from typing import Optional


def extract_code(text: str) -> Optional[str]:
    """
    Extract a code block enclosed by triple backticks from the given text.

    Args:
        text (str): The text containing the code block.

    Returns:
        Optional[str]: The extracted code block or None if no code block is found.
    """
    code_block_pattern = re.compile(r"```(?:python)?\s*\n(.*?)\n```", re.DOTALL)
    match = code_block_pattern.search(text)

    if match:
        return match.group(1).strip()
    return None
