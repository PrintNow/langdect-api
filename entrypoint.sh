#!/bin/sh

set -e

# default behaviour is to launch redis-server
if [[ -z ${1} ]]; then
  echo "Starting langdetect-api..."
  exec python src/main.py
else
  echo "Executing command: $@"
  exec "$@"
fi
