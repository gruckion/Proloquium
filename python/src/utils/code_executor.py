import os

import docker


def execute_python_file(file: str, workspace_folder="project"):
    """Execute a Python file in a Docker container

    Args:
        file (str): The file to execute

    Returns:
        str: The output of the execution
    """

    if not file.endswith(".py"):
        return "Error: Invalid file type. Only .py files are allowed."

    file_path = os.path.join(workspace_folder, file)

    if not os.path.isfile(file_path):
        return f"Error: File '{file}' does not exist."

    try:
        client = docker.from_env()

        container = client.containers.run(
            "python:3.9.16-slim-bullseye",
            f"python {file}",
            volumes={
                os.path.abspath(workspace_folder): {"bind": "/workspace", "mode": "ro"}
            },
            working_dir="/workspace",
            stderr=True,
            stdout=True,
            detach=True,
        )

        output = container.wait()
        print(f"output: {output}")
        logs = container.logs().decode("utf-8")
        container.remove()

        return logs

    except Exception as error:
        return f"Error: {str(error)}"
