This is a demo event that reads in the events package.

## Container Installation 
* Have docker desktop running
* Clone repo and open in container with VS code (container should build automatically)
* OR open repo in GitHub code spaces 
* Run command `poetry update` in terminal after container/codespace is built

## Runing Dev WebApp 
* In ‘ksu-events-demo' run the command `poetry run python manage.py migrate` 
* Then run the command `poetry run python manage.py runserver 0.0.0.0:8000` 
* Open [localhost:8000](localhost:8000) in a web browser
