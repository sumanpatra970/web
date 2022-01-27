release: python manage.py migrate

web: daphne -b 0.0.0.0 -p 8001 web.asgi:application
worker: python manage.py runworker channels --settings=core.settings -v2
