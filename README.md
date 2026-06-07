# TeamBoard Knowledge Base API

A Django REST Framework based Knowledge Base API with JWT Authentication, PostgreSQL and Docker.

## Features

- User Registration
- User Login
- JWT Authentication
- Company Management
- API Key Generation using Django Signals
- Knowledge Base Search
- Query Logging
- Usage Analytics Dashboard
- PostgreSQL Integration
- Docker Support
- Django Admin Panel

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- JWT (SimpleJWT)

## API Endpoints

### Register
POST /api/auth/register/

### Login
POST /api/auth/login/

### Query Knowledge Base
POST /api/kb/query/

### Usage Summary
GET /api/admin/usage-summary/

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/udhayasa0507-stackly/teamboard-knowledge-base-api.git
cd teamboard-knowledge-base-api
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
DB_NAME=teamboard
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=django-secret-key
DEBUG=True
```

### Start PostgreSQL with Docker

```bash
docker-compose up -d
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

## Seed Knowledge Base Entries

Add KBEntry records using:

- Django Admin Panel
- PostgreSQL Database
- Django Shell

Example Topics:

- JWT
- JWT Authentication
- DRF
- PostgreSQL
- Docker
- Q Objects
- transaction.atomic()
- select_related()
- prefetch_related()
- Django Signals

## Authentication

JWT Authentication is enabled globally using SimpleJWT.

Public Endpoints:

- Register
- Login

Protected Endpoints:

- Query Knowledge Base
- Usage Summary

## Author

**Udhaya Sankar**
