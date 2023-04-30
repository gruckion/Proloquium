import docker
from docker.models.containers import Container


def start_container(working_dir: str, volumes) -> Container:
    """
    Pulls the desired Docker image, creates and runs a Docker container in detached mode.
    
    Returns:
        Container: A Docker container object.
    """
    client = docker.from_env()
    image_name = "python:3-alpine"
    client.images.pull(image_name)
    return client.containers.run(
        image_name, detach=True,
        tty=True,
        stdin_open=True,
        working_dir=working_dir,
        volumes=volumes,
    )


def execute_command(container: Container, user_command: str) -> tuple[bytes, bytes]:
    """
    Executes a given command against the specified Docker container.
    
    Args:
        container (Container): The Docker container object.
        user_command (str): The command to run inside the container.
    
    Returns:
        Tuple[bytes, bytes]: The stdout and stderr of the executed command.
    """
    exec_result = container.exec_run(user_command, stdout=True, stderr=True, demux=True)
    stdout, stderr = exec_result.output
    return stdout, stderr


def shutdown_container(container: Container) -> None:
    """
    Stops and removes the specified Docker container.
    
    Args:
        container (Container): The Docker container object.
    """
    container.stop()
    container.remove()
