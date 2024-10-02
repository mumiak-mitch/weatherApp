#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies using Pipenv
pipenv install --deploy --ignore-pipfile

# Collect static files
python manage.py collectstatic --no-input

# Remove the migration command since no database is needed
# python manage.py migrate  # This line is no longer needed

# Create superuser if the environment variable is set
if [[ $CREATE_SUPERUSER ]]; then
  python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi