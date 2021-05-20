#!/usr/bin/env bash
# start-server.sh

./web/wait-for-it.sh db:5432
./web/setup.sh
python3 manage.py collectstatic --no-input
python3 manage.py makemigrations --no-input
python3 manage.py migrate
python3 manage.py createsuperuser --no-input


gunicorn --user www-data -b 0.0.0.0:8010 -w 3 RemoteCompute.wsgi:application

exec "$@"