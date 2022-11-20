#!/bin/sh
python manage.py collectstatic --no-input --clear
#python manage.py createsuperuser --noinput --username alchercaadmin --email alcher@gmail.com
python manage.py migrate
# python manage.py createsuperuser --noinput --firstname admin --email admin@admin.com
gunicorn parliamentarydebate.wsgi:application --preload --bind 0.0.0.0:80 --log-level=debug --timeout 180  --workers 4