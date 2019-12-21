#!/bin/bash
python manage.py collectstatic
/usr/local/bin/uwsgi --socket :3031 --wsgi-file /home/docker/app/api/wsgi.py --py-autoreload 3
