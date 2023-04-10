import functools

from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate

from common.config import settings
from utils.code_executor import execute_python_file
from utils.extract_code import extract_code

random_prompt = PromptTemplate(
    template="""
Write the code for the first task.

```

{task}
```

Declarative, Immutable, pythonic, design patterns, solid, and ensure 100% unit test coverage. Use the latest Python typing support.
Include docstrings everywhere and a docstring for the file on line 1.
Respond only with the files e.g.

Example:

```filename.py
# code here
```
    """,
    input_variables=["task"],
)


# @functools.lru_cache(maxsize=None)
def get_chains(chat, prompt_system):
    """Get the chain of prompts for the chat

    Args:
        chat (Chat): The chat model
        prompt_system (PromptTemplate): The system prompt

    Returns:
        LLMChain: The chain of prompts
    """
    system_message = SystemMessagePromptTemplate(prompt=prompt_system)
    chat_prompt = ChatPromptTemplate.from_messages([system_message])
    ai_chain = LLMChain(llm=chat, prompt=chat_prompt)
    return ai_chain


def main() -> None:
    """
    Main function that takes a task input from the user and sends it to api_request function.
    """
    # task = input("Enter the task: ")

    task = """
        Create Input and Output CSV Processors
        Description: Develop a CSVProcessor class with methods to read input CSV, process it, and generate an output CSV. This class should follow the Single Responsibility Principle and be designed to handle only CSV processing tasks.
    """

    chat = ChatOpenAI(temperature=0.7, max_tokens=1000)

    random_chain = get_chains(chat, random_prompt)

    random_run = random_chain.run(
        task=task,
    )

    print(random_run)

    save_python_file("random.py", extract_code(random_run))

    execute_python_file("random.py")


def save_python_file(file_name: str, code: str):
    """Save python file to project folder

    Args:
        file_name (str): The name of the file
        code (str): The code to save
    """
    with open(f"project/{file_name}", "w", encoding="utf-8") as file:
        file.write(code)


if __name__ == "__main__":
    main()
