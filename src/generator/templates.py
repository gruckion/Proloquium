from langchain.prompts import PromptTemplate

from src.utilities.file_loader import load_file_content


def create_template_from_file(file_path: str) -> PromptTemplate:
    """
    Create a PromptTemplate from the content of a file.

    Args:
        file_path (str): The path to the template file.

    Returns:
        PromptTemplate: A PromptTemplate instance with the template content.
    """
    template_content = load_file_content(file_path)
    return PromptTemplate(
        input_variables=["task_description", "project_name"],
        template=template_content,
    )
