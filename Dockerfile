FROM python:3.8-slim

LABEL author="Gabriel Carneiro <carneiro.development@gmail.com>"

ENV FLASK_APP=run.py
ENV APPLICATION_ENV=Production
ENV FLASK_PORT=5010

RUN apt-get update

RUN python --version && pip --version
RUN pip install poetry

RUN mkdir /app

COPY ./flask_auth app/flask_auth
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

CMD gunicorn -c flask_auth/gunicorn.conf.py flask_auth.run:app
