#!/bin/sh

python manage.py collectstatic --no-input
gunicorn django_store.wsgi:application --bind 0.0.0.0:8000 & wait