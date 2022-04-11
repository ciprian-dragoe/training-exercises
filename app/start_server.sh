#!/usr/bin/env bash
case "$FLASK_ENV" in
 development) python /app/app.py ;;
           *) service nginx start
#              todo: this is unsafe for a prod environment, give www-data acess to the docker socker
              chmod 666 /var/run/docker.sock
              uwsgi --ini uwsgi.ini;;
esac
