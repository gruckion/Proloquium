"""Environment variables for the application"""

from pydantic import BaseSettings


class EnvironmentVariables(BaseSettings):
    """Default settings for the application"""

    ENVIRONMENT: str
    OPENAI_API_KEY: str
    OPENAI_API_MODEL: str
    OPENAI_TEMPERATURE: float
    OPENAI_MAX_TOKENS: int
    PINECONE_API_KEY: str
    PINECONE_ENVIRONMENT: str
    TABLE_NAME: str
    OBJECTIVE: str
    INITIAL_TASK: str

    class Config:
        """Pydantic config class"""

        case_sensitive = True


settings = EnvironmentVariables()
