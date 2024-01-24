# sample-django


python3 -m venv venv
. venv/bin/activate
pip3 install django
django-admin startproject demoproject
cd demoproject 
python3 manage.py startapp demoapp
python3 manage.py runserver