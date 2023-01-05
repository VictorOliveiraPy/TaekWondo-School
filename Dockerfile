# pull official base image
FROM python:3.10.1-slim-buster

# set working directory
WORKDIR /

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock ./
COPY . /



RUN poetry config virtualenvs.create false \
    && poetry install --only main
