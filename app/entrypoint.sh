#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Uncomment to clear all previous data
python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata ui/fixtures/data.json ui/fixtures/users.json
python manage.py collectstatic --no-input --clear

exec "$@"
