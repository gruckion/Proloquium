import os

from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = "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"


def create_chat_model(temperature=0.5):
    return OpenAI(temperature=temperature)
