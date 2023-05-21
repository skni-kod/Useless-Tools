#!/bin/sh
gunicorn siteproject.wsgi:application --bind 127.0.0.1:8000 & \
nginx -g 'daemon off;' &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?