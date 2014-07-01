#!/bin/bash

source venv/bin/activate
./venv/bin/pip install -U -r requisitos.txt
cd webserver
gunicorn webserver.wsgi:application --workers=3
