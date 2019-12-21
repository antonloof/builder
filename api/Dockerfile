FROM python:3.7

RUN pip install uwsgi
COPY requirements.txt /home/docker/app/requirements.txt
RUN pip install -r /home/docker/app/requirements.txt

COPY urls.py /home/docker/app/urls.py
COPY manage.py /home/docker/app/manage.py
COPY docker-entrypoint.sh /home/docker/app/docker-entrypoint.sh

WORKDIR /home/docker/app/
ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]
