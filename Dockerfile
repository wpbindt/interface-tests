FROM python:3.11-slim-buster

RUN pip install pytest==7.2.1 mypy==0.991

WORKDIR /srv
