# TeamBoard Knowledge Base API

A Django REST Framework based Knowledge Base API with JWT Authentication, PostgreSQL and Docker.

## Features

* User Registration
* User Login
* JWT Authentication
* Company Management
* API Key Generation using Django Signals
* Knowledge Base Search
* Query Logging
* Usage Analytics
* PostgreSQL Integration
* Docker Support
* Django Admin Panel

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* Docker
* JWT (SimpleJWT)

## API Endpoints

### Register

POST `/api/auth/register/`

### Login

POST `/api/auth/login/`

### Query Knowledge Base

POST `/api/kb/query/`

### Usage Summary

GET `/api/admin/usage-summary/`

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Author

Udhaya Sankar
