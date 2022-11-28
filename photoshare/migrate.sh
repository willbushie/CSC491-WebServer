#!/bin/bash

# ONLY RUN THIS SCRIPT INSIDE OF VIRTUAL ENVIRONMENT

# make migrations and migrate - must be completed before starting server
python manage.py makemigrations
python manage.py migrate
