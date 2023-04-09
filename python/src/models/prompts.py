"""Prompts for the different roles in the scrum process."""

import os
from enum import Enum

from models.roles import Role


class Prompt(Enum):
    """Prompts for the different roles in the scrum process."""

    EXECUTIVE_SPONSOR = "EXECUTIVE_SPONSOR"
    PRODUCT_OWNER = "PRODUCT_OWNER"
    PROJECT_MANAGER = "PROJECT_MANAGER"
    LEAD_ENGINEER = "LEAD_ENGINEER"
    SOFTWARE_ARCHITECT = "SOFTWARE_ARCHITECT"
    BACKEND_DEVELOPER = "BACKEND_DEVELOPER"
    FRONTEND_DEVELOPER = "FRONTEND_DEVELOPER"
    FULL_STACK_DEVELOPER = "FULL_STACK_DEVELOPER"
    MOBILE_DEVELOPER = "MOBILE_DEVELOPER"
    QA_ENGINEER = "QA_ENGINEER"
    CLOUD_ENGINEER = "CLOUD_ENGINEER"
    DEVOPS_ENGINEER = "DEVOPS_ENGINEER"
    UI_UX_DESIGNER = "UI_UX_DESIGNER"
    TECHNICAL_WRITER = "TECHNICAL_WRITER"
    DATA_SCIENTIST_ENGINEER = "DATA_SCIENTIST_ENGINEER"
    SECURITY_ENGINEER = "SECURITY_ENGINEER"
    BUSINESS_ANALYST = "BUSINESS_ANALYST"
    SCRUM_MASTER_AGILE_COACH = "SCRUM_MASTER_AGILE_COACH"

    @staticmethod
    def load_prompt(role: Role, prompt: str) -> str:
        """Loads the prompt for the given role."""
        prompt_file_path = f"python/data/prompt/{role.name.lower()}/{prompt}.prompt"

        if os.path.isfile(prompt_file_path):
            with open(prompt_file_path, "r", encoding="utf-8") as prompt_file:
                return prompt_file.read().strip()
