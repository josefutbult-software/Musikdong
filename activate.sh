#!/usr/bin/env bash

source venv/bin/activate
export FLASK_APP=code/app.py
export FLASK_ENV=development
flask run