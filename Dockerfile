FROM python:3.11.2

RUN python3 -m pip install --upgrade pip
RUN pip install poetry

RUN useradd -ms /bin/bash widgets

COPY --chown=widgets . /365widgets/
COPY 365widgets/pyproject.toml poetry.lock /
RUN poetry install --no-dev \
    && rm pyproject.toml poetry.lock

WORKDIR 365widgets
USER widgets