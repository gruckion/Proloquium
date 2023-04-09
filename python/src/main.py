"""A simple command line application that runs a background process."""

import cmd
import threading
import time

from models.prompts import Prompt

# from models.prompts import Prompt
from models.roles import Role
from utils.openai_utils import openai_call

# from utils.openai_utils import openai_call


class BackgroundProcess(threading.Thread):
    """A background process that runs for 10 seconds."""

    def __init__(self, objective):
        super().__init__()
        self.objective = objective
        self.status = "Not started"
        self.done = False

    def run(self):
        self.status = "In progress"
        # Simulating a long-running process
        time.sleep(10)
        self.status = f"Completed: {self.objective}"
        self.done = True


def communicate(prompt: str):
    """Communicate with the OpenAI API."""

    loaded_prompt = Prompt.load_prompt(Role.PRODUCT_OWNER, prompt)
    response = openai_call(loaded_prompt)
    return response


class CommandLineApp(cmd.Cmd):
    """A simple command line application that runs a background process."""

    roles = list(Role.__members__)
    responses = {}

    intro = communicate("discovery_call")

    print(intro)
    prompt = "> "

    def __init__(self):
        super().__init__()
        self.bg_process = None

    def do_start(self, objective):
        """Start a background process for the given objective."""
        if not self.bg_process or self.bg_process.done:
            self.bg_process = BackgroundProcess(objective)
            self.bg_process.start()
            print(f"Started process for objective: {objective}")
            self.process_objective(objective)
        else:
            print("Another process is already running")

    def do_update(self, _):
        """Update the status of the background process."""
        if self.bg_process:
            print(f"Status: {self.bg_process.status}")
        else:
            print("No process running")

    def do_exit(self, _):
        """Exit the application."""
        if self.bg_process and not self.bg_process.done:
            print("Waiting for the background process to finish")
            self.bg_process.join()
        print("Exiting...")
        return True

    def process_objective(self, objective: str):
        """Process the objective by passing it between roles."""
        self.responses = {}
        for role in self.roles:
            print(f"{role} sees the objective: {objective}")
            response = input(f"{role} response: ")
            self.responses[role] = response
            if role != self.roles[-1]:
                print(f"Previous responses: {self.responses}")
                input("Press Enter to continue")
        print(f"Summary: {', '.join(self.responses.values())}")


if __name__ == "__main__":
    print("Starting the application")
    app = CommandLineApp()
    app.cmdloop()
