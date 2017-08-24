#!/bin/bash

set -e

HOST=banana.foodsharing.de

BRANCH=$TRAVIS_BRANCH

if [ -z "$BRANCH" ]; then
  BRANCH=$(git rev-parse --abbrev-ref HEAD)
fi

echo "deploying branch [$BRANCH] to [$HOST]"

if [ "$BRANCH" = "master" ]; then
  scp deploy/deploy-uwsgi.sh fslight@$HOST:deploy-wsgi.sh
  ssh fslight@$HOST ./deploy-wsgi.sh "$BRANCH"
fi
