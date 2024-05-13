"""
Django settings for gymception project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
import dj_database_url



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-0ia3+@ggt9&1n&&p76f5h*abq&x+=((@e$z5w(dum!ma%2&)0-"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#allowing all hosts
ALLOWED_HOSTS = ["*", '172.20.10.3']

#CSRF TRUSTED ORIGINS
CSRF_TRUSTED_ORIGINS = ['http://*', 'https://localhost:8000']


# Application definition

INSTALLED_APPS = [
    "daphne", 
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "members",
    "fontawesomefree",
    "django_celery_beat",
    "push_notifications",
    "channels"
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = "gymception.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "gymception.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('STACKHERO_MYSQL_DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

DATABASES['default']['OPTIONS'] = {
    'ssl': {
        'ca': '/workspaces/Gymception/ca.pem',
        'cert': '/workspaces/Gymception/client-cert.pem',
        'key': '/workspaces/Gymception/client-key.pem'
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

#setting time zone to local time zone
TIME_ZONE = "America/Phoenix"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/\\

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#ASGI application
ASGI_APPLICATION = "gymception.asgi.application"

#VAPID_KEYS
VAPID_PUBLIC_KEY = "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEnKPiA+31hqAjX69CiAXW6OujqN15vxxeanMCncMccxWiK7q0VfKzfw3WGs2UiH+hDH3KVJksxY00f7IYErL0Dw=="
VAPID_PRIVATE_KEY = "MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgwSaGndmGlzHHko0zmO+9a9JbOUfP8HP7pWQG+ovZo26hRANCAASco+ID7fWGoCNfr0KIBdbo66Oo3Xm/HF5qcwKdwxxzFaIrurRV8rN/DdYazZSIf6EMfcpUmSzFjTR/shgSsvQP"
VAPID_ADMIN_EMAIL = "sbeeredd@asu.edu"
VAPID_APPLICATION_SERVER_KEY = "BJyj4gPt9YagI1-vQogF1ujro6jdeb8cXmpzAp3DHHMVoiu6tFXys38N1hrNlIh_oQx9ylSZLMWNNH-yGBKy9A8"

#login redirect
LOGIN_URL = 'login'

# gymception/settings.py

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'remove_expired_queue_entries': {
        'task': 'members.tasks.remove_expired_queue_entries',
        'schedule': crontab(minute='*/1'),
    },
    'clear_expired_queues': {
        'task': 'members.tasks.clear_expired_queues',
        'schedule': crontab(minute='*/1'),
    },
}

# Configure the Channel Layer
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],  # Assuming Redis is running on localhost and default port
        },
    },
}

django_heroku.settings(locals())