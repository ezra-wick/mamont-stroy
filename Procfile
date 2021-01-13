web: gunicorn mamontov.wsgi --log-file -
celery: celery -A mamontov worker -l info -P gevent
