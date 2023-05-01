import re

from src.generator.file_writer import FileData


def extract_file_name_and_code(text: str) -> list[FileData]:
    file_name_pattern = re.compile(r"File:\s*`(.+?)`")
    code_block_pattern = re.compile(r"```(?:python)?\s*\n(.*?)\n```", re.DOTALL)

    file_name_matches = list(file_name_pattern.finditer(text))
    code_block_matches = list(code_block_pattern.finditer(text))

    result = []

    if len(file_name_matches) == len(code_block_matches):
        for file_name_match, code_block_match in zip(
            file_name_matches, code_block_matches
        ):
            file_name = file_name_match.group(1)
            code_block = code_block_match.group(1).strip()
            result.append((file_name, code_block))

    return result
