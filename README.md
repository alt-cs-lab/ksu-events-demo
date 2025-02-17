This is a demo event that reads in the events package.

## Container Installation
* Have docker desktop running
* Clone repo and open in container with VS code (container should build automatically)
* OR open repo in GitHub code spaces 

## Runing Dev WebApp
* migrate the db `poetry run python manage.py migrate` 
* start the server `poetry run python manage.py runserver`
* optionally specify port `poetry run python manage.py runserver 0.0.0.0:8000`
* open the provided URL in a web browser `Starting development server at http://0.0.0.0:8000/`

## Common Commands
* update dependencies and lock file (pyproject.toml and poetry.lock) to latest version `poetry update`
* make migrations `poetry run python manage.py makemigrations`
* manage db `poetry run python manage.py dbshell`
* creating admin account `poetry run python manage.py createsuperuser`

## Reset DB when migrations fail
* manage db `poetry run python manage.py dbshell`
* drop schema `DROP SCHEMA public CASCADE;`
* recreate schema `CREATE SCHEMA public;`
* leave psql `\q`
* optionally create migrations `poetry run python manage.py makemigrations`
* migrate db `poetry run python manage.py migrate` 

## login to django admin panel
* creating admin account `poetry run python manage.py createsuperuser`
* run server `poetry run python manage.py runserver`
* go to admin panel `/admin`
