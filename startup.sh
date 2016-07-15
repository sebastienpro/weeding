#!/usr/bin/env bash
set -e

./manage.py migrate
exec /usr/local/bin/gunicorn mariage.wsgi:application -w 4 -b :8000