#!/bin/bash

set -e

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

BRANCH=$1
backend_dir=/var/www/fslight/www/foodsharing-django-api
touch_reload=/var/run/foodsharing-django-api.reload

if [ -z "$BRANCH" ]; then
  echo "Please pass branch to deploy as first argument"
  exit 1
fi

# expects that project is cloned into backend directory
# expects that virtualenv is set up
# manually: virtualenv --python=python3 --no-site-packages ${backend_dir}/env

# expects local_settings.py to exist
# use local_settings.py.example as template

(
  cd ${backend_dir} && \
  git clean -fd && \
  git checkout "$BRANCH" && \
  git pull && \
  env/bin/pip-sync && \
  env/bin/python manage.py migrate && \
  env/bin/python manage.py check --deploy && \
  env/bin/python manage.py collectstatic --clear --no-input && \
)

touch ${touch_reload}
