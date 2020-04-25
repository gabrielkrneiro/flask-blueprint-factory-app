FROM python:3.8.2-alpine3.11

LABEL author="GabrielCarneiroDeveloper"

CMD ["mkdir", "/app"]

COPY ./flask_auth /app/flask_auth
COPY ./run.py /app/run.py
COPY ./gunicorn.conf.py /app/gunicorn.conf.py
COPY ./setup.py /app/setup.py
COPY ./Makefile /app/Makefile

ENV FLASK_APP=run.py
ENV APPLICATION_ENV=Production

WORKDIR /app

RUN ["ls", "-latr"]

ENTRYPOINT ["make", "runserver-prod"]