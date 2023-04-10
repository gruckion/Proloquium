import subprocess

from pygments.lexers import get_lexer_for_filename


def process_file(file_path):
    # Identify language
    lexer = get_lexer_for_filename(file_path)
    language = lexer.name

    # Generate tags using ctags
    subprocess.run(["ctags", "-f", "tags", file_path])

    # Read the generated tags file and parse symbols
    with open("tags", "r") as tags_file:
        symbols = [line.split("\t")[0] for line in tags_file.readlines()]

    return language, symbols
