import asyncio
import json
import logging

import chainlit as cl
from dotenv import load_dotenv
from jsonrpcclient import Ok, parse_json, request_json
from langchain import LLMChain, OpenAI, PromptTemplate
from websockets.client import connect

load_dotenv()

TEMPLATE = """Question: {question}

Answer: Let's think step by step."""


@cl.langchain_factory
def factory():
    llm = OpenAI(temperature=0, streaming=True)
    prompt = PromptTemplate(template=TEMPLATE, input_variables=["question"])
    return LLMChain(prompt=prompt, llm=llm, verbose=True)


@cl.on_chat_start
def start():
    file = None

    # Wait for the user to upload a file
    while file is None:
        file = cl.AskFileMessage(
            content="Please upload a text file to begin!",
            accept=["*"],
            max_size_mb=10,
        ).send()
    # Decode the file
    text = file.content.decode("utf-8")

    # Let the user know that the system is ready
    cl.Message(
        content=f"`{file.name}` uploaded, it contains {len(text)} characters!"
    ).send()

    cl.Message(
        content=f"```python\n{text}",
    ).send()

    # Create a new event loop
    new_event_loop = asyncio.new_event_loop()
    # Set the new event loop as the current event loop
    asyncio.set_event_loop(new_event_loop)
    # Run the main function using the new event loop
    initialize = new_event_loop.run_until_complete(main())

    if initialize is not None:
        # Pretty format the JSON response
        initialize_json = json.dumps(initialize.result, indent=4)
        cl.Message(
            content=f"```json\n{initialize_json}",
        ).send()

async def main() -> None:
    """Handle request"""
    async with connect("ws://localhost:2087") as socket:
        await socket.send(request_json("initialize"))
        response = parse_json(await socket.recv())

    if isinstance(response, Ok):
        print(response.result)
        return response

    logging.error(response.message)
    return None
