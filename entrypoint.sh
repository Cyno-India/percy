# #!/bin/sh

# python manage.py migrate --noinput
# python manage.py collectstatic --noinput

# gunicorn sales.wsgi:application --bind 0.0.0.0:8000

#!/bin/sh

set -e

ls -la /vol/
ls -la /vol/web

whoami

python manage.py collectstatic --noinput
python manage.py migrate

# uwsgi --socket :9000 --workers 4 --master --enable-threads --module sales.wsgi
gunicorn sales.wsgi:application --bind 0.0.0.0:8000
