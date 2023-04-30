FROM python:3.9

RUN pip install poetry
RUN poetry config virtualenvs.create false
WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root

COPY . /app/
