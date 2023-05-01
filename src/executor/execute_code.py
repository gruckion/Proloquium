import docker
from docker.models.containers import Container, ExecResult


def start_container(working_dir: str, volumes) -> Container:
    """
    Pulls the desired Docker image,
    creates and runs a Docker container in detached mode.

    Returns:
        Container: A Docker container object.
    """
    client = docker.from_env()
    image_name = "python:3-alpine"
    client.images.pull(image_name)
    return client.containers.run(
        image_name,
        detach=True,
        tty=True,
        stdin_open=True,
        working_dir=working_dir,
        volumes=volumes,
    )


def execute_command(container: Container, user_command: str) -> ExecResult:
    """
    Executes a given command against the specified Docker container.

    Args:
        container (Container): The Docker container object.
        user_command (str): The command to run inside the container.

    Returns:
        ExecResult: The result of the command execution.
    """
    return container.exec_run(user_command, stdout=True, stderr=True, stream=True)


def shutdown_container(container: Container) -> None:
    """
    Stops and removes the specified Docker container.

    Args:
        container (Container): The Docker container object.
    """
    container.stop()
    container.remove()
