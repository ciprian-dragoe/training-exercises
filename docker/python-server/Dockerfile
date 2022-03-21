# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
RUN mkdir /app
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY . /app
CMD [ "python", "/app/server.py" ]
