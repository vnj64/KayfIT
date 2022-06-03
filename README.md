# KayfIT
A project for "RPM Python", named "KayfIT" - restourant.
Comands for starting using a project and server:

* pip install -r requirements.txt
* docker run --name kayfit -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=rest_db -p 45678:5432 -d postgres
* python3 manage.py makemigrations
* python3 manage.py migrate
* python3 manage.py createsuperuser
* python3 manage.py runserver
