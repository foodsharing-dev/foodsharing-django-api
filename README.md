# foodsharing-django-api
A clean start with a foodsharing API project in python/django.

## Installing

You need python and preferrably a virtualenv.

Most developers use bleeding edge python while we currently use python 3.4 in production.

For the MySQL library, the following packages under debian are needed:

```
apt-get install python3-dev libmysqlclient-dev
```

Create a virtualenv, install pip-tools and the dependencies:

```
cd foodsharing-django-api
virtualenv --no-site-packages -p /usr/bin/python3 env
. ./env/bin/activate
pip install pip-tools
pip-sync
```

## Database
This backend is supposed to work together with the existing [foodsharing.de] database.
Currently, it is not configured to create the necessary database by itself.

The foodsharing.de PHP application is quite easy to setup using docker-compose,
but unfortunately not yet available open source.

Please request access at [https://gitlab.com/foodsharing-dev] and follow the instructions
for setup.

`local_settings.py.example` contains the database configuration necessary to talk to the
database inside the docker container.

It is important for us to enable a good developer experience although at this stage it is still
complicated to completely decouple the projects. It is still likely that this will be happening in
the next months, further help on this is highly appreciated

##
