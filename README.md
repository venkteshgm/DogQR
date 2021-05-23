# DogQR

The plan is to build a landing site whose link is loaded into QR codes strapped on your furry friends.

pip3 install django==2.1.5

create virtual environment with
	virtualenv -p python3 .
start your virtual environment with
	source bin/activate

django-admin startproject DogQR .

python3 manage.py runserver

python3 manage.py migrate

python3 manage.py createsuperuser
	venktesh venktesh

python3 manage.py startapp <app_name>

python3 manage.py makemigrations

Anytime any changes are made to models.py of any app, the following commands need to be run:
	python3 manage.py makemigrations
	python3 manage.py migrate