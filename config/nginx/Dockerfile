# syntax = docker/dockerfile:experimental
FROM nginx:latest
MAINTAINER "Jonah Winchell" "jonahwinchell@gmail.com"

COPY default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log
CMD ./setup.sh
STOPSIGNAL SIGTERM