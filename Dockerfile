FROM curlimages/curl:latest AS curl-stage
# Recommended way to install Poetry package manages, according to the documentation
RUN curl -sSL https://install.python-poetry.org -o /tmp/get-poetry.py

FROM python:3.11.2

RUN python3 -m pip install --upgrade pip

COPY --from=curl-stage /tmp/get-poetry.py /tmp/get-poetry.py

RUN python /tmp/get-poetry.py --version 1.4.0
ENV PATH="${PATH}:/root/.local/bin"
# Making poetry use the global python of the container
RUN poetry config virtualenvs.create false

RUN useradd -ms /bin/bash widgets

COPY pyproject.toml poetry.lock /
RUN poetry install --no-dev \
    && rm pyproject.toml poetry.lock
# ^ to be pedantic and space-savey about it, i guess we dont want two copies of the poetry files laying around the container

COPY --chown=widgets . /app/

WORKDIR /app

# dont buffer output from flask;
# ensures output when logging func is called rather than buffering and being lost if process crashes
ENV PYTHONUNBUFFERED TRUE

USER widgets

CMD ["gunicorn", "-c", "conf/gunicorn-cfg.py", "..."]