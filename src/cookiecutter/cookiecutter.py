from datetime import datetime, timezone
import os
from typing import Literal

from cookiecutter.main import cookiecutter
from pydantic import BaseModel

from src.cookiecutter.templates import CookiecutterTemplate
from src.generator.proloquium__project_dir import prolouqium_project_dir


class ProjectContext(BaseModel):
    time_stamp: str
    project_name: str
    author_name: str
    repo_name: str

    full_name: str
    email: str
    github_name: str
    project_slug: str
    module_name: str
    short_description: str
    version: str
    license: Literal["MIT", "GPL-3.0-or-later", "Proprietary"]
    command_line_interface: Literal["no cli", "click"]
    use_jupyterlab: bool
    add_badges: bool


def create_project(template: CookiecutterTemplate, extra_context: ProjectContext) -> str:
    project_name = extra_context["project_name"]

    print(f"Creating project: {project_name}")
    extra_context = {
        **extra_context,
        "time_stamp": datetime.now(timezone.utc).isoformat(),
        "full_name": "John Doe",
        "email": "john.doe@example.com",
        "github_name": "johndoe",
        "module_name": project_name.replace("-", "_"),
        "short_description": "A short description of the project.",
        "version": "0.0.1",
        "license": "MIT",
        "command_line_interface": "no cli",
        "use_jupyterlab": "n",
        "add_badges": "y",
        "repo_name": "my_project",
        "project_slug": project_name.replace("_", "-"),
    }

    output_dir = prolouqium_project_dir()

    # Create the project using the specified template, context, and output directory
    cookiecutter(
        template=template.value, checkout=None, no_input=True, extra_context=extra_context, output_dir=output_dir
    )

    return os.path.join(output_dir, project_name)
