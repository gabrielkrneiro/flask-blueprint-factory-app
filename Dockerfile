FROM gabucarneiro/ubuntu_python38:1

LABEL author="Gabriel Carneiro <carneiro.development@gmail.com>"

ENV FLASK_APP=run.py
ENV APPLICATION_ENV=Production
ENV FLASK_PORT=5010

RUN ["mkdir", "/app"]

COPY ./dist /app/dist
COPY ./Makefile /app/Makefile

WORKDIR /app


RUN tar -zxvf dist/flask_auth-0.1.0.tar.gz && \
    mv flask_auth-0.1.0/* . && \
    rm -rf flask_auth-0.1.0 && \
    /root/.pyenv/shims/python /app/setup.py install

EXPOSE 5010

# CMD /bin/bash
CMD ["make", "runserver-prod"]