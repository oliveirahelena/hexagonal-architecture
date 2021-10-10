# pull official base image
FROM python:3.9.7-alpine3.14

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
COPY ./requirements-dev.txt .
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc git libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install --upgrade pip
RUN pip install -r requirements-dev.txt
RUN apk del .tmp-build-deps

RUN adduser --disabled-password --uid 1000 python

RUN mkdir /app

USER python

WORKDIR /app

# add app
COPY . .
