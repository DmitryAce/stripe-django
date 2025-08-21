#!/bin/bash
set -e

echo "Applying migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Django server..."
exec gunicorn --bind 0.0.0.0:5000 ecommerce_store.wsgi:application --access-logfile access.log --error-logfile error.log