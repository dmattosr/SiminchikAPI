FROM python:3.8.10

RUN apt-get update

ADD . /app

WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
