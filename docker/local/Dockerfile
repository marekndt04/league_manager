FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements/local.txt /app/
RUN apt-get update && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r local.txt

COPY ./docker/local/start.sh /start.sh
RUN chmod +x /start.sh
COPY . /app/