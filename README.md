# Sample Dockerized Django app

This is a tiny application I wrote to begin learning how to use Django.


```
python3 -m venv venv
. venv/bin/activate
pip3 install django
django-admin startproject demoproject
cd demoproject 
python3 manage.py startapp demoapp
python3 manage.py runserver
```