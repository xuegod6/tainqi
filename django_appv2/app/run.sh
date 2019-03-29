#!/bin/bash
python /var/www/src/tianqi/manage.py makemigrations
python /var/www/src/tianqi/manage.py migrate
uwsgi --ini /var/www/uwsgi.ini
