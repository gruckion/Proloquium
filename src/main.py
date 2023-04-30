import click

from langchain.chains import LLMChain
from src.cookiecutter.cookiecutter import create_project
from src.cookiecutter.templates import CookiecutterTemplate
from src.executor.execute_code import execute_command, shutdown_container, start_container
from src.extractor.code_extractor import extract_file_name_and_code
from src.generator.file_writer import save_files
from src.generator.templates import create_template_from_file
from src.utilities.chat_model import create_chat_model
from src.utilities.random_project_name import random_project_name


@click.command()
@click.option(
    "--task-description",
    default="Print 'Hello, World!'",
    help="The task description for the Python program.",
)
def main(task_description: str):
    project_name = random_project_name()

    # Generate the initial Python program
    project_path = create_project(template=CookiecutterTemplate.DEFAULT, extra_context={"project_name": project_name})

    # Load the template and chat model
    template = create_template_from_file("src/prompts/code.md")
    chat_model = create_chat_model()

    # Generate the code for the task description
    chain = LLMChain(llm=chat_model, prompt=template)
    response = chain.run(task_description=task_description, project_name=project_name)

    # Extract the files from the response and save them
    code = extract_file_name_and_code(response)
    save_files(project_path, code)

    click.echo(response)
    print(code)

    # Define working directory inside the container
    container_working_dir = "/app"

    # Configure volumes
    volumes = {
        project_path: {"bind": container_working_dir, "mode": "rw"}
    }

    container = start_container(container_working_dir, volumes)

    while True:
        # apk add --no-cache make
        # curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
        user_command = input("> ")

        if user_command == "exit":
            break

        stdout, stderr = execute_command(container, "apk add --no-cache make curl poetry")
        stdout, stderr = execute_command(container, user_command)

        if stdout:
            print(stdout.decode("utf-8"))
        if stderr:
            print(stderr.decode("utf-8"))

    shutdown_container(container)
