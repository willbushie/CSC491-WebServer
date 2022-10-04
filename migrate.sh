#!/bin/bash

# ONLY RUN THIS SCRIPT INSIDE OF VIRTUAL ENVIRONMENT

python manage.py makemigrations
python manage.py migrate
