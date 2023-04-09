"""Main module."""

from common.config import settings
from utils.task_management import TaskManager


def main():
    """Main function."""
    print("Starting task manager...")

    print("\033[94m\033[1m" + "\n*****OBJECTIVE*****\n" + "\033[0m\033[0m")
    print(f"{settings.OBJECTIVE}")

    print(
        "\033[93m\033[1m"
        + "\nInitial task:"
        + "\033[0m\033[0m"
        + f" {settings.INITIAL_TASK}"
    )

    task_manager = TaskManager(
        objective=settings.OBJECTIVE, initial_task=settings.INITIAL_TASK
    )
    task_manager.run()


if __name__ == "__main__":
    main()
