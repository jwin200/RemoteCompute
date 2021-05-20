# syntax = docker/dockerfile:experimental
FROM python:slim-buster
MAINTAINER "Jonah Winchell" "jonahwinchell@gmail.com"

RUN mkdir -p /opt/app && \
    mkdir -p /opt/app/pip_cache
WORKDIR /opt/app
COPY ./config ./src /opt/app/
RUN chmod +x web/start-server.sh && \
    chmod +x web/wait-for-it.sh && \
    chmod +x web/setup.sh && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt --cache-dir pip_cache && \
    chown -R www-data:www-data /opt
CMD ./web/start-server.sh
STOPSIGNAL SIGTERM