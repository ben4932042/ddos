FROM python:3.6-alpine

MAINTAINER ben0824

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "main.py" ]
