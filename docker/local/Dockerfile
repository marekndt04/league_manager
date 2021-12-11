FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
  # Python packages dependencies
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # clean up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY ./requirements /requirements
RUN apt-get update && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r /requirements/local.txt \
    && rm -rf /requirements


COPY ./docker/local/start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh
RUN chmod +x /start.sh
