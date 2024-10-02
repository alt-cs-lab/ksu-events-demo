This is a demo event that reads in the events package.

setup for development within devcontainer

## Container Installation 
* Have docker desktop running
* Clone repo and open in an instance of VS code (container should build automatically)
* OR open repo in GitHub code spaces 

## Runing Dev WebApp 
* In ‘ksu-events-demo' run the command `python manage.py migrate` 
* Then run the command `python manage.py runserver 0.0.0.0:8000` 
* Open [localhost:8000](localhost:8000) in a web browser