# tests/unit/generator/test_templates.py
import os
import tempfile

from src.generator.templates import create_template_from_file


def test_create_template_from_file():
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as test_file:
        test_file.write(
            "This is a test template with {task_description} and project name {project_name}."
        )
        test_file_path = test_file.name

    template = create_template_from_file(test_file_path)

    # Clean up the temporary file
    os.remove(test_file_path)

    formatted_str = template.format(
        task_description="some value", project_name="fluffy-bunny"
    )
    assert (
        formatted_str
        == "This is a test template with some value and project name fluffy-bunny."
    )
