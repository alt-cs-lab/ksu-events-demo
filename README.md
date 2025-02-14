This is a demo event that reads in the events package.

## Container Installation
* Have docker desktop running
* Clone repo and open in container with VS code (container should build automatically)
* OR open repo in GitHub code spaces 

## Runing Dev WebApp
* In 'ksu-events-demo' run the command `poetry run python manage.py migrate` 
* Then run the command `poetry run python manage.py runserver 0.0.0.0:8000` 
* Open [localhost:8000](localhost:8000) in a web browser

## Common Commands
* update dependencies (in pyproject.toml) to latest version `poetry update`
* make migrations `poetry run python manage.py makemigrations`
* manage db `poetry run python manage.py dbshell`

## Reset DB when migrations fail
* manage db `poetry run python manage.py dbshell`
* drop schema `DROP SCHEMA public CASCADE;`
* recreate schema `CREATE SCHEMA public;`
* leave psql `\q`
* optionally create migrations `poetry run python manage.py makemigrations`
* migrate db `poetry run python manage.py migrate` 
