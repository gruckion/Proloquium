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

    builder = load_project("file:///Users/sigex/workdir/proloquium/")

    initialize = builder.initialize_payload()

    # Create a new event loop
    new_event_loop = asyncio.new_event_loop()
    # Set the new event loop as the current event loop
    asyncio.set_event_loop(new_event_loop)
    # Run the main function using the new event loop
    initialize = new_event_loop.run_until_complete(lsp_send(initialize))

    if initialize is not None:
        initialize_json = json.dumps(initialize.result, indent=4)
        cl.Message(
            content=f"```json\n{initialize_json}",
        ).send()

        # Create the text_document_symbols_payload
        symbols_payload = builder.build_text_document_symbols_payload("file_uri")  # replace with the correct file_uri
        symbols_payload_response = new_event_loop.run_until_complete(lsp_send(symbols_payload))

        if symbols_payload_response is not None:
            symbols_payload_response_json = json.dumps(symbols_payload_response.result, indent=4)
            cl.Message(
                content=f"```json\n{symbols_payload_response_json}",
            ).send()

def load_project(root_path: str):
    """Load a project"""
    return LSPRequestBuilder(root_path)


async def lsp_send(request) -> None:
    """Handle request"""
    async with connect("ws://localhost:2087") as socket:

        await socket.send(request)
        response = parse_json(await socket.recv())

    if isinstance(response, Ok):
        print(response.result)
        return response

    logging.error(response.message)
    return None


class LSPRequestBuilder:
    """Build LSP request payloads"""

    def __init__(self, root_path: str):
        self.root_path = root_path

    def initialize_payload(self):
        return request_json("initialize", {
            "rootPath": self.root_path,
            "initializationOptions": {}
        })

    def build_text_document_did_open_payload(self, language_id: str, file_uri: str, file_content: str):
        return request_json("textDocument/didOpen", {
            "textDocument": {
                "uri": file_uri,
                "languageId": language_id,
                "version": 1,
                "text": file_content
            }
        })

    def build_text_document_language_payload(self, language_id, file_uri: str, file_content: str):
        return request_json("textDocument/didOpen", {
            "textDocument": {
                "uri": file_uri,
                "languageId": language_id,
                "version": 1,
                "text": file_content
            }
        })

    def build_text_document_symbols_payload(self, file_uri: str):
        return request_json("textDocument/documentSymbol", {
            "textDocument": {
                "uri": file_uri
            }
        })

    def build_text_document_formatting_payload(self, file_uri: str, tab_size, insert_spaces):
        return request_json("textDocument/formatting", {
            "textDocument": {
                "uri": file_uri
            },
            "options": {
                "tabSize": tab_size,
                "insertSpaces": insert_spaces
            }
        })

    def build_text_document_code_action_payload(self, file_uri: str, line, character):
        return request_json("textDocument/codeAction", {
            "textDocument": {
                "uri": file_uri
            },
            "range": {
                "start": {
                    "line": line,
                    "character": character
                },
                "end": {
                    "line": line,
                    "character": character
                }
            },
            "context": {
                "diagnostics": []
            }
        })

    def build_text_document_hover_payload(self, file_uri: str, line, character):
        return request_json("textDocument/hover", {
            "textDocument": {
                "uri": file_uri
            },
            "position": {
                "line": line,
                "character": character
            }
        })

    def build_text_document_references_payload(self, file_uri: str, line, character):
        return request_json("textDocument/references", {
            "textDocument": {
                "uri": file_uri
            },
            "position": {
                "line": line,
                "character": character
            },
            "context": {
                "includeDeclaration": True
            }
        })

    def build_text_document_definition_payload(self, file_uri: str,  line, character):
        return request_json("textDocument/definition", {
            "textDocument": {
                "uri": file_uri
            },
            "position": {
                "line": line,
                "character": character
            }
        })

    def build_text_document_highlights_payload(self, file_uri: str, line, character):
        return request_json("textDocument/documentHighlight", {
            "textDocument": {
                "uri": file_uri
            },
            "position": {
                "line": line,
                "character": character
            }
        })

    def build_text_document_completion_payload(self, file_uri: str, line, character, trigger_character=None):
        payload = {
            "textDocument": {
                "uri": file_uri
            },
            "position": {
                "line": line,
                "character": character
            },
            "context": {
                "triggerKind": 1  # Trigger completion manually
            }
        }
        if trigger_character:
            payload["context"]["triggerCharacter"] = trigger_character
        return request_json("textDocument/completion", payload)
