"""Utility functions for interacting with the OpenAI API."""


import functools
import os
import pickle
import subprocess
import time

import openai

from common.config import settings

openai.api_key = settings.OPENAI_API_KEY


@functools.lru_cache(maxsize=None)
def openai_call(
    prompt: str,
    model: str = settings.OPENAI_API_MODEL,
    temperature: float = settings.OPENAI_TEMPERATURE,
    max_tokens: int = settings.OPENAI_MAX_TOKENS,
) -> str:
    """
    Make a call to the OpenAI API to generate a response based on the given
    prompt, model, temperature, and max_tokens.

    Args:
        prompt (str): The input prompt for the OpenAI API.
        model (str, optional): The model to be used for generating the response
        Defaults to OPENAI_API_MODEL.
        temperature (float, optional): Controls the randomness of the response.
        Defaults to 0.5.
        max_tokens (int, optional): Maximum number of tokens in the response.
        Defaults to 100.

    Returns:
        str: The generated response from the OpenAI API.
    """
    while True:
        try:
            if model.startswith("llama"):
                cmd = ["llama/main", "-p", prompt]
                result = subprocess.run(
                    cmd,
                    shell=True,
                    check=True,
                    stderr=subprocess.DEVNULL,
                    stdout=subprocess.PIPE,
                    text=True,
                )
                return result.stdout.strip()

            if not model.startswith("gpt-"):
                response = openai.Completion.create(
                    engine=model,
                    prompt=prompt,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                )
                return response.choices[0].text.strip()

            messages = [{"role": "user", "content": prompt}]
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                n=1,
                stop=None,
            )
            return response.choices[0].message.content.strip()
        except openai.error.RateLimitError:
            print("The OpenAI API rate limit has been exceeded.")
            print("Waiting 10 seconds and trying again...")
            time.sleep(10)


@functools.lru_cache(maxsize=None)
def get_ada_embedding(text: str):
    """Get the embedding for a given text using the Ada model."""
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model="text-embedding-ada-002")[
        "data"
    ][0]["embedding"]
