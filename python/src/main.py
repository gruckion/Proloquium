"""Main module"""

import os

import openai
from dotenv import load_dotenv


def main():
    """Main function"""

    load_dotenv()

    # Read API key from environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Set up the API request parameters
    prompt = "Once upon a time in a land far, far away..."
    max_tokens = 50
    temperature = 0.8

    # Make the API request
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        n=1,
        stop=None,
        echo=False,
    )

    # Extract and print the generated text
    generated_text = response.choices[0].text
    print(generated_text)


if __name__ == "__main__":
    main()
