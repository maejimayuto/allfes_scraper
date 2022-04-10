FROM python:3.9

WORKDIR /allfes_scraper
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH=$POETRY_HOME/bin:$VENV_PATH/bin:$PATH

COPY pyproject.toml poetry.lock ./
RUN poetry install
