release: python manage.py migrate
web: daphne web.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=web.settings -v2
heroku config:set DISABLE_COLLECTSTATIC=1