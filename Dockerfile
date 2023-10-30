FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY parseq_requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r parseq_requirements.txt

RUN apt update && apt install -y vim

COPY . .
