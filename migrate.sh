#!/bin/bash

# ONLY RUN THIS SCRIPT INSIDE OF VIRTUAL ENVIRONMENT

cd ./photoshare
python manage.py makemigrations
python manage.py migrate
cd ..