#!/usr/bin/env sh

set -e

host="$1"
shift
cmd="$@"

export PGPASSWORD='DBPWDCHANGEMEONINSTALL'
# celery as root
export C_FORCE_ROOT='true'
until psql -h "$host" -U "cloudlaunch" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

python manage.py migrate
python manage.py createsuperuser
celery -A cloudlaunch worker --detach -l info

exec $cmd

