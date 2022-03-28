#!/usr/bin/env bash
if [ "$FLASK_ENV" == "development" ]
then
#  service nginx start
#  uwsgi --ini uwsgi.ini --touch-reload /app/ # if running from windows hot reloading is not working the standard way and this works
  python /app/app.py
else
  service nginx start
  uwsgi --ini uwsgi.ini
fi

