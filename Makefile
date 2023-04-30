.PHONY: all format lint test tests test_watch integration_tests help

all: help

coverage:  # run unit tests and generate coverage report
	poetry run pytest --cov \
		--cov-report xml:cov.xml \
		--cov-report term-missing:skip-covered

format:  # run code formatters
	poetry run black .
	poetry run ruff --select I --fix .

PYTHON_FILES=.
lint: PYTHON_FILES=.
lint_diff: PYTHON_FILES=$(shell git diff --name-only --diff-filter=d master | grep -E '\.py$$')

lint lint_diff:  # run linters
	poetry run mypy $(PYTHON_FILES)
	poetry run black $(PYTHON_FILES) --check
	poetry run ruff .

test:  # run unit tests
	poetry run pytest tests/unit

tests:  # run unit tests with verbose output
	poetry run pytest -s tests/unit

test_watch:  # run unit tests in watch mode
	poetry run ptw --now . -- tests/unit

integration_tests:  # run integration tests
	poetry run pytest tests/integration

e2e_tests:  # run e2e tests
	poetry run pytest tests/e2e

help: # show the help message
	@echo 'Available targets:'
	@echo ''
	@grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
