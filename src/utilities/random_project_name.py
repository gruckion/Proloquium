from faker import Faker

fake = Faker()


def random_project_name() -> str:
    """_summary_

    Returns:
        str: random project name
    """

    return fake.word().lower()
