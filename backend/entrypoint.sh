#!/bin/sh

cd /app/backend

#python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input

gunicorn --workers=3 --bind 0.0.0.0:8080 backend.wsgi
