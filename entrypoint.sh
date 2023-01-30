#!/bin/sh

echo "Create static root folder"
mkdir -p /static_data
echo "Makemigrations"
python manage.py makemigrations
echo "Migrate DB"
python manage.py migrate --no-input
echo "Collect statics"
python manage.py collectstatic --no-input

exec "$@"