release: python manage.py migrate
web: gunicorn project.wsgi --bind 0.0.0.0:$PORT