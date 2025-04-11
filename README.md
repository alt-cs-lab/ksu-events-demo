This is a demo event that reads in the events package.

## Container Installation
* Have docker desktop running
* Clone repo and open in container with VS code (container should build automatically)
* OR open repo in GitHub code spaces 

## Update Events Package (While developing)
1. `Ctrl+X` 'ksu-events' in pyproject.toml (should be line 11)
2. run `poetry lock` in terminal
3. run `poetry sync` in terminal
4. re-paste the 'ksu-events' line in pyproject.toml
5. run `poetry lock` in terminal
6. run `poetry sync` in terminal
- You can change the package version in toml by branch name (i.e branch="main") or by release tag (i.e tag="a.8.0")

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
