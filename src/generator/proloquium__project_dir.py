import os


def prolouqium_project_dir():
    home_dir = os.path.expanduser("~")

    return os.path.join(home_dir, "proloquium-projects")
