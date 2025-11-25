#!/usr/bin/env bash
# Render build script

python manage.py collectstatic --noinput
python manage.py migrate --noinput
