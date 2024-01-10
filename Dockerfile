FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /neoquiz_app
COPY poetry.lock pyproject.toml /neoquiz_app/
RUN pip install -U pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install
COPY . ./
COPY ../.env ./.env
EXPOSE 8000
