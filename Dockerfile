FROM python:3.12-slim

WORKDIR /code

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false

COPY . /code/

RUN poetry install --no-root --no-dev --no-interaction --no-ansi

EXPOSE 8000

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "core.asgi:application"]