from unittest.mock import patch

import pytest

from src.executor.execute_code import (
    execute_command,
    shutdown_container,
    start_container,
)


# Setup mock Docker client and container
@pytest.fixture
def mock_docker():
    with patch("src.executor.execute_code.docker") as mock_docker:
        mock_docker.from_env().images.pull.return_value = "pulled_image"
        mock_docker.from_env().containers.run.return_value = "run_container"
        yield mock_docker


@pytest.fixture
def mock_container():
    with patch("src.executor.execute_code.Container", autospec=True) as mock_container:
        mock_container.exec_run.return_value = "exec_result"
        mock_container.stop.return_value = None
        mock_container.remove.return_value = None
        yield mock_container


def test_start_container(mock_docker):
    result = start_container("test_dir", {"vol1": {}})
    mock_docker.from_env().images.pull.assert_called_once_with("python:3-alpine")
    mock_docker.from_env().containers.run.assert_called_once_with(
        "python:3-alpine",
        detach=True,
        tty=True,
        stdin_open=True,
        working_dir="test_dir",
        volumes={"vol1": {}},
    )
    assert result == "run_container"


def test_execute_command(mock_container):
    result = execute_command(mock_container, "test_command")
    mock_container.exec_run.assert_called_once_with(
        "test_command", stdout=True, stderr=True, stream=True
    )
    assert result == "exec_result"


def test_shutdown_container(mock_container):
    shutdown_container(mock_container)
    mock_container.stop.assert_called_once()
    mock_container.remove.assert_called_once()
