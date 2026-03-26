# django-project

Enter your database password (YOUR_PASSWORD).

BACKEND SETUP (Django + MySQL)
====================================

Install venv module and activate

YOUR_WORKSPACE_PATH> python -m venv post-env  
YOUR_WORKSPACE_PATH> post-env\Scripts\activate  

Install Django

(post-env) YOUR_WORKSPACE_PATH> python -m pip install Django  

To know the version

(post-env) YOUR_WORKSPACE_PATH> django-admin --version  

Create a project

(post-env) YOUR_WORKSPACE_PATH> django-admin startproject myapp  

Start the project server

YOUR_WORKSPACE_PATH\myapp> python manage.py runserver  

Deployment files available:
- asgi.py
- wsgi.py

------------------------------------

Create an app

YOUR_WORKSPACE_PATH\myapp> python manage.py startapp blog  

Register app in settings.py

File: YOUR_WORKSPACE_PATH\myapp\myapp\settings.py  

Add in INSTALLED_APPS:

'blog',

------------------------------------

Connect MySQL DB to Django

(post-env) YOUR_WORKSPACE_PATH> pip install mysqlclient  
(post-env) YOUR_WORKSPACE_PATH> pip list  

Update database config:

File: YOUR_WORKSPACE_PATH\myapp\myapp\settings.py  

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'YOUR_MYSQL_DB_NAME',
        'USER': 'root',
        'PASSWORD': 'YOUR_PASSWORD',
        'HOST': 'localhost',   # or your server IP
        'PORT': '3306'
    }
}

------------------------------------

Create Migrations and Apply

(post-env) YOUR_WORKSPACE_PATH\myapp> python manage.py makemigrations  
(post-env) YOUR_WORKSPACE_PATH\myapp> python manage.py migrate  

------------------------------------

Create Fake Data (Optional)

(post-env) YOUR_WORKSPACE_PATH\myapp> pip install faker  

Run custom commands:

(post-env) YOUR_WORKSPACE_PATH\myapp> python manage.py populates_posts  
(post-env) YOUR_WORKSPACE_PATH\myapp> python manage.py populates_categories  

------------------------------------

Install Pagination (Optional)

(post-env) YOUR_WORKSPACE_PATH\myapp> pip install django-pagination  

------------------------------------

Create Superuser

(post-env) YOUR_WORKSPACE_PATH\myapp> python manage.py createsuperuser  

------------------------------------

Run Backend Server

(post-env) YOUR_WORKSPACE_PATH\myapp> python manage.py runserver  

Backend URL:
http://127.0.0.1:8000/

====================================
FRONTEND SETUP
====================================

Go to frontend folder

YOUR_WORKSPACE_PATH> cd frontend  

Install dependencies

YOUR_WORKSPACE_PATH\frontend> npm install  

Start frontend server

YOUR_WORKSPACE_PATH\frontend> npm start  

OR (if using Vite)

YOUR_WORKSPACE_PATH\frontend> npm run dev  

Frontend URL:
http://localhost:3000/  
OR  
http://localhost:5173/  

====================================
CONNECT FRONTEND & BACKEND
====================================

- Backend runs on: http://127.0.0.1:8000/
- Use API URLs in frontend (example):
  http://127.0.0.1:8000/api/

------------------------------------

Enable CORS in Django

(post-env) YOUR_WORKSPACE_PATH\myapp> pip install django-cors-headers  

Update settings.py:

INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True

Reference:
https://youtu.be/g5vFWHajutg
