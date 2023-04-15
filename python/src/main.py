import functools
import os
from datetime import datetime

from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate

from common.config import settings
from utils.code_executor import execute_python_file
from utils.extract_code import extract_file_name_and_code
from utils.file_reader import read_file_content
from utils.pytest_exector import run_pytest

code_generator = PromptTemplate(
    template=read_file_content("../prompts/code_generator.txt"),
    input_variables=["task"],
)

unit_test_generator = PromptTemplate(
    template=read_file_content("../prompts/unit_test_generator.txt"),
    input_variables=["file_name", "code"],
)


# @functools.lru_cache(maxsize=None)
def get_chains(chat, prompt):
    """Get the chain of prompts for the chat

    Args:
        chat (Chat): The chat model
        prompt (PromptTemplate): The system prompt

    Returns:
        LLMChain: The chain of prompts
    """
    system_message = SystemMessagePromptTemplate(prompt=prompt)
    chat_prompt = ChatPromptTemplate.from_messages([system_message])
    ai_chain = LLMChain(llm=chat, prompt=chat_prompt)
    return ai_chain


def main() -> None:
    """
    Main function that takes a task input from the user and sends it to api_request function.
    """
    print("Welcome to the Code Generator!")
    # task = input("Enter the task: ")

    # task = """
    #     Create Input and Output CSV Processors
    #     Description: Develop a CSVProcessor class with methods to read input CSV, process it, and generate an output CSV.
    #     This class should follow the Single Responsibility Principle and be designed to handle only CSV processing tasks.
    # """

    task = """
        Create functions for add, subtract, divide and mupliply
    """

    chat = ChatOpenAI(temperature=0.7, max_tokens=1000)

    code_generator_chain = get_chains(chat, code_generator)

    code_generator_run = code_generator_chain.run(
        task=task,
    )

    print(f"Generated response: {code_generator_run}")

    file_name, code = extract_file_name_and_code(code_generator_run)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    save_file(f"logs/{timestamp}/{file_name}.prompt", code_generator_run)
    save_file(f"logs/{timestamp}/{file_name}", code)

    save_file(f"project/{file_name}", code)

    execute_python_file(file_name)

    unit_test_generator_chain = get_chains(chat, unit_test_generator)

    unit_test_generator_run = unit_test_generator_chain.run(
        file_name=file_name,
        code=code,
    )

    print(f"Generated response: {unit_test_generator_run}")

    file_name, code = extract_file_name_and_code(unit_test_generator_run)

    save_file(f"logs/{timestamp}/{file_name}.prompt", unit_test_generator_run)
    save_file(f"logs/{timestamp}/{file_name}", code)

    save_file(f"project/{file_name}", unit_test_generator_run)

    test_result = run_pytest(f"logs/{timestamp}/")

    save_file(f"logs/{timestamp}/result_{file_name}.txt", test_result)


def save_file(file_name: str, code: str):
    """Save python file to project folder

    Args:
        file_name (str): The name of the file
        code (str): The code to save
    """
    print(f"Saving {file_name} to project folder")

    directory = os.path.dirname(file_name)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(code)


if __name__ == "__main__":
    main()
