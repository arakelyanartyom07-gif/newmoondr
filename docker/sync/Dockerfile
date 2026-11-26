FROM python:3.13-alpine

RUN apk add --no-cache \
    curl \
    bash \
    ca-certificates \
    rclone \
    postgresql-client \
    unzip

RUN pip install --no-cache-dir \
    apscheduler \
    boto3

WORKDIR /app