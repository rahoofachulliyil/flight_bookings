# Use an official Python image as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies to be able to build packages
RUN apt-get update \
    && apt-get install -y curl build-essential libpq-dev

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Ensure Poetry is available in PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock /app/

# Install Python dependencies via Poetry
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application code
COPY . /app/

# Expose the port that the Django app will run on
EXPOSE 8000

# Run the Django development server
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
