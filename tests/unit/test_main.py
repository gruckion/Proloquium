# tests/unit/test_main.py
import pytest
from click.testing import CliRunner
from langchain.llms.fake import FakeListLLM

from src.main import main


@pytest.fixture(autouse=True)
def mock_llmchain(mocker) -> FakeListLLM:
    responses = ["Mocked code output"]
    fake_llm = FakeListLLM(responses=responses)
    mocker.patch("src.main.create_chat_model", return_value=fake_llm)
    return fake_llm


def test_main_default_task_description(mock_llmchain: FakeListLLM):
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "Mocked code output" in result.output
    assert mock_llmchain.i == 1


def test_main_custom_task_description(mock_llmchain: FakeListLLM):
    runner = CliRunner()
    task_description = "Calculate the sum of 3 and 5"
    result = runner.invoke(main, ["--task-description", task_description])
    assert result.exit_code == 0
    assert "Mocked code output" in result.output
    assert mock_llmchain.i == 1


def test_main_empty_task_description(mock_llmchain: FakeListLLM):
    runner = CliRunner()
    task_description = ""
    result = runner.invoke(main, ["--task-description", task_description])
    assert result.exit_code == 0
    assert "Mocked code output" in result.output
    assert mock_llmchain.i == 1


def test_main_complex_task_description(mock_llmchain: FakeListLLM):
    runner = CliRunner()
    task_description = "Create a function that reverses a given string"
    result = runner.invoke(main, ["--task-description", task_description])
    assert result.exit_code == 0
    assert "Mocked code output" in result.output
    assert mock_llmchain.i == 1
