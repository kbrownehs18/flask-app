#!/bin/sh
gunicorn -c gunicorn.py --access-logfile - --error-logfile - -D --worker-class gevent run:app
/usr/local/openresty/nginx/sbin/nginx -g "daemon off;"
