# Specify full version security best practice
FROM python:3.9.16-slim-bullseye as base

# Ensures that the container uses the UTF-8 character set. This is recommended for Python 3
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
# Disables the writing of .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Enables the Python fault handler
ENV PYTHONFAULTHANDLER 1

# Build stage for installing compilation dependencies
FROM base AS builder

# Install compilation dependencies and ensure that all packages in the image are up to date
RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc=4:10.2.1-1 \
  libffi-dev=3.3-6 \
  linux-libc-dev=5.10.158-2 \
  build-essential=12.9 \
  # Clean up apt cache to reduce image size
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Build stage for installing python dependencies
FROM builder AS python-deps

# Install pipenv uses Docker cache only reduce image size
RUN python -m pip install pipenv==2023.2.18 --no-cache-dir

# Set working directory
WORKDIR /

# Copy only the Pipfiles and install dependencies
COPY ./Pipfile ./
COPY ./Pipfile.lock ./
RUN PIPENV_VENV_IN_PROJECT=1 python -m pipenv install --deploy

# Build stage for running the application
FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
# Set virtual env path
ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
VOLUME /home/appuser
USER appuser

# Install application into container
COPY ./ ./

# Run the application
ENTRYPOINT ["python", "-m", "src.main"]
