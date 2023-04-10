# import os
# import tempfile

# from ctags import CTags, TagEntry
# from pygments import highlight
# from pygments.formatters import NullFormatter
# from pygments.lexers import get_lexer_by_name, guess_lexer_for_filename
# from pygments.token import Token


# def list_imports(file_path, code, language):
#     imports = []

#     lexer = get_lexer_by_name(language, stripall=True)
#     formatter = NullFormatter()
#     tokens = [(t[0], t[1]) for t in lexer.get_tokens(code)]

#     for i, (token_type, token_value) in enumerate(tokens):
#         if token_type == Token.Keyword.Namespace and token_value in ("import", "from"):
#             import_line = token_value
#             j = i + 1
#             while tokens[j][0] != Token.Text:
#                 import_line += tokens[j][1]
#                 j += 1
#             imports.append(import_line.strip())

#     print(f"Imports:\n{imports}\n")


# def identify_decorators(file_path, code, language):
#     if language.lower() != "python":
#         print("Decorator identification only supported for Python.")
#         return

#     decorators = {}

#     lexer = get_lexer_by_name(language, stripall=True)
#     formatter = NullFormatter()
#     tokens = [(t[0], t[1]) for t in lexer.get_tokens(code)]

#     current_decorator = None
#     for token_type, token_value in tokens:
#         if token_type == Token.Name.Decorator:
#             current_decorator = token_value
#         elif token_type == Token.Name.Function and current_decorator:
#             if token_value not in decorators:
#                 decorators[token_value] = []
#             decorators[token_value].append(current_decorator)
#             current_decorator = None

#     print(f"Decorators:\n{decorators}\n")


# def identify_symbols(file_path):
#     with open(file_path, "r") as file:
#         code = file.read()

#     # Identify the language
#     lexer = guess_lexer_for_filename(file_path, code)
#     language = lexer.name
#     print(f"Language: {language}")

#     list_imports(file_path, code, language)
#     identify_decorators(file_path, code, language)

#     # Generate tags file
#     with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#         temp_file_path = temp_file.name

#     os.system(f"ctags -o {temp_file_path} {file_path}")

#     # Process tags file
#     tags = CTags(temp_file_path)
#     entry = TagEntry()

#     while tags.next(entry):
#         print(f"{entry['kind']}: {entry['name']}")

#     # Clean up
#     os.remove(temp_file_path)


# # Usage:
# identify_symbols("python/src/utils/pinecone_utils.py")

import json
import os
from pathlib import Path


def get_target_folder():
    while True:
        target_folder = input("Enter the path of the folder you want to target: ")
        if os.path.isdir(target_folder):
            return target_folder
        return "/Users/sigex/workdir/backend"


def get_ignore_folders():
    ignore_file = ".proloquiumignore"
    ignore_folders = set()
    if os.path.isfile(ignore_file):
        with open(ignore_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    ignore_folders.add(line)
    return ignore_folders


def get_directory_list(target_folder: str, ignore_folders: set) -> list:
    """
    Returns a list of unique subdirectory names for the given target folder,
    and all its subdirectories recursively.

    Args:
        target_folder (str): The path to the target folder.
        ignore_folders (set): A set of folder names to ignore.

    Returns:
        list: A list of unique subdirectory names for the given target folder.
    """
    path = Path(target_folder)
    subdirs = []
    for subpath in path.iterdir():
        if subpath.is_dir() and subpath.name not in ignore_folders:
            subdirs.append(subpath.name)
            subdirs.extend(get_directory_list(str(subpath), ignore_folders))
    return list(set(subdirs))


def get_directory_structure(target_folder: str, ignore_folders: set) -> dict:
    """
    Returns a dictionary representing the directory structure of the target folder.
    Only subdirectories of the target folder are included in the dictionary, and the
    function is recursive, so all subdirectories of the target folder are also included.
    Any directories specified in the ignore_folders set are excluded from the directory
    structure.

    Args:
        target_folder (str): The path to the target folder.
        ignore_folders (set): A set of folder names to ignore.

    Returns:
        dict: A dictionary representing the directory structure of the target folder.
    """
    path = Path(target_folder)
    return {
        path.name: {
            folder.name: get_directory_structure(str(folder), ignore_folders)
            for folder in path.iterdir()
            if folder.is_dir() and folder.name not in ignore_folders
        }
        for path in path.iterdir()
        if path.is_dir() and path.name not in ignore_folders
    }


def get_files_list(target_folder: str, ignore_folders: set) -> list:
    """
    Returns a list of unique file names in the target folder and its subfolders.
    Any directories specified in the ignore_folders set are excluded.

    Args:
        target_folder (str): The path to the target folder.
        ignore_folders (set): A set of folder names to ignore.

    Returns:
        list: A list of unique file names in the target folder and its subfolders.
    """

    path = Path(target_folder)
    if path.is_file():
        return [path.name]
    else:
        result = []
        for file in sorted(path.glob("*")):
            if file.is_dir() and file.name not in ignore_folders:
                result += get_files_list(str(file), ignore_folders)
            elif file.is_file():
                result.append(file.name)
        return list(set(result))


def get_files_structured(target_folder: str, ignore_folders: set) -> dict:
    """
    Returns a dictionary representing the files in the target folder.
    Only files in the target folder are included in the dictionary, and the
    function is recursive, so all files in the target folder are also included.
    Any directories specified in the ignore_folders set are excluded from the directory
    structure.

    Args:
        target_folder (str): The path to the target folder.
        ignore_folders (set): A set of folder names to ignore.

    Returns:
        dict: A dictionary representing the files in the target folder.
    """

    path = Path(target_folder)
    if path.is_file():
        return {path.name: path.stat().st_size}
    else:
        result = {}
        for file in sorted(path.glob("*")):
            if file.is_dir() and file.name not in ignore_folders:
                result[file.name] = get_files_structured(str(file), ignore_folders)
            elif file.is_file():
                result[file.name] = file.stat().st_size
        return result


def save_dict_to_json(dictionary: dict, filename: str):
    filename = f"{filename}.json"
    with open(filename, "w") as f:
        json.dump(dictionary, f, indent=4)


if __name__ == "__main__":
    target_folder = get_target_folder()

    ignore_folders = get_ignore_folders()

    directory_list = get_directory_list(target_folder, ignore_folders)
    save_dict_to_json(directory_list, "directory_list")

    directory_structure = get_directory_structure(target_folder, ignore_folders)
    save_dict_to_json(directory_structure, "directory_structure")

    files_list = get_files_list(target_folder, ignore_folders)
    save_dict_to_json(files_list, "directory_files_list")

    files = get_files_structured(target_folder, ignore_folders)
    save_dict_to_json(files, "directory_files_structure")
