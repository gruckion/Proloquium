"""
Extract Code Module
-------------------

This module contains the extract_code function, which is responsible for extracting a specific code block
from a given text. The function searches for a code block enclosed by triple backticks (```) and returns
the contents within it.
"""

import re
from typing import Optional, Tuple


def extract_file_name_and_code(text: str) -> Optional[Tuple[str, str]]:
    """Extract a file name and code block from the given text.

    Args:
        text (str): The text containing the file name and code block.

    Returns:
        Optional[Tuple[str, str]]: A tuple containing the file name and code block or None if no file name
    """
    file_name_pattern = re.compile(r"\[(.+)\]")
    code_block_pattern = re.compile(r"```(?:python)?\s*\n(.*?)\n```", re.DOTALL)

    file_name_match = file_name_pattern.search(text)
    code_block_match = code_block_pattern.search(text)

    if file_name_match and code_block_match:
        file_name = file_name_match.group(1)
        code_block = code_block_match.group(1).strip()
        return (file_name, code_block)
    return None
