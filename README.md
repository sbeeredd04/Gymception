# Gymception Application Setup

This document outlines the necessary steps to set up and run the Gymception application with its Celery task queue.

## Prerequisites

Before starting, ensure you have the following installed:
- Python (3.7 or later)
- Redis server (for Celery broker)
- Virtual environment tool (like venv or virtualenv)

## Initial Setup

1. **Clone the repository:**
   ```sh
   git clone <repository-url>

## Set up a virtual environment:

python -m venv venv
Activate the virtual environment:

### On Windows:
```.\venv\Scripts\activate```

### On Unix or MacOS:
```source venv/bin/activate```

## Install the dependencies:
```pip install -r requirements.txt```

## Set up environment variables:

Create a .env file in the root of your project and set up the necessary environment 

variables, such as SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASE_URL, and any other variables 

required for the settings.

## Database Setup

Run migrations to create the database schema:
```python manage.py makemigrations```
```python manage.py migrate ```

## Running Redis Server
Ensure Redis server is running as it is required for Celery:
redis-server

## Running Celery Worker
To handle background tasks, start the Celery worker by running:
```celery -A gymception worker -l info```

## Running Celery Beat
For periodic tasks, you will need to run Celery beat as well:
```celery -A gymception beat -l info```

## Running the Django Development Server
Finally, you can start the Django development server:

```python manage.py runserver```

# Admin Panel
To access the Django admin panel and manage the application, navigate to 
http://localhost:8000/admin/. 

To use the admin panel, you must first create a superuser:
```python manage.py createsuperuser```

Follow the prompts to set up the superuser, then log in with these credentials on the admin site.

## Additional Information
To access the application, go to http://localhost:8000/.
To stop the server or Celery worker, use CTRL+C in the terminal.
Always ensure the virtual environment is activated when working with the project.
For production environments, be sure to configure a more robust message broker and result backend for Celery, such as RabbitMQ or Amazon SQS.