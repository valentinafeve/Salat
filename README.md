# Salat

## Installing django

> Once Python and pip is installed

```bash
pip install django
pip install django-rest-framework
pip install django-rest-auth
```

## Setting the database

```sql
CREATE DATABASE Salat;
CREATE USER 'django'@'localhost' IDENTIFIED BY 'sSal281sT';
GRANT ALL PRIVILEGES ON Salat TO 'django'@'localhost';
```

## Running Django

```bash
python manage.py migrate
python manage.py createsuper
python manage.py runserver
```

Project developed for educational purposes. Passwords shouldn't be added in a repository.
