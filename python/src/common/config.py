"""Environment variables for the application"""
import os

from dotenv import load_dotenv

load_dotenv()


class EnvironmentVariables:
    """Default settings for the application"""

    ENVIRONMENT = os.getenv("ENVIRONMENT")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_API_MODEL = os.getenv("OPENAI_API_MODEL")
    OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE") or 0.5)
    OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS") or 100)
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
    TABLE_NAME = os.getenv("TABLE_NAME")
    SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

    OBJECTIVE = os.getenv("OBJECTIVE")
    INITIAL_TASK = os.getenv("INITIAL_TASK")


settings = EnvironmentVariables()
