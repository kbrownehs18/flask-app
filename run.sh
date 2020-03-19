#!/bin/sh
/usr/local/openresty/nginx/sbin/nginx &
gunicorn -c gunicorn.py --access-logfile - --error-logfile - --worker-class gevent run:app
