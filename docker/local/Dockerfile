FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app/

RUN apt-get update \
  # Python packages dependencies
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # git for locall development
  && apt-get install -y git \
  # clean up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

ARG USERNAME=user-app
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN apt-get update && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r ./requirements/local.txt

COPY ./docker/local/start.sh ./start.sh
RUN sed -i 's/\r$//g' ./start.sh
RUN chmod +x ./start.sh
