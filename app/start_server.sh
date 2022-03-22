#!/usr/bin/env bash
if [ "$FLASK_ENV" == "development" ]
then
#  service nginx start
#  uwsgi --ini uwsgi.ini --touch-reload /app/
  python /app/app.py
else
  service nginx start
  uwsgi --ini uwsgi.ini
fi

