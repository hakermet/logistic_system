"""
Django settings for logistics_system project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8&79808x8eruv_cjq5q16(4v4i!i+#!%$&utcgm40i_rcw^l@q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

import os
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Custom apps
    'users',
    'orders',
    'routes',
    'rest_framework',  # Django REST Framework
    'telegram_bot',
]


MIDDLEWARE = [
    'csp.middleware.CSPMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

CSP_DEFAULT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "'unsafe-eval'",
    "https:",
    "data:",
)
CSP_SCRIPT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "'unsafe-eval'",
    "https://maps.googleapis.com",
    "https://*.googleapis.com",
    "https://*.google.com",
    "https://*.gstatic.com",
    "https://cdn.jsdelivr.net",
    "https://*.jsdelivr.net",
    "https://code.jquery.com",
    "https://api.mapbox.com",  # Додано
    "https://*.mapbox.com"     # Додано
)
CSP_IMG_SRC = (
    "'self'",
    "data:",
    "https:",
    "https://*.mapbox.com",    # Додано
    "https://api.mapbox.com"   # Додано
)
CSP_CONNECT_SRC = (
    "'self'",
    "https:",
    "https://api.mapbox.com/",  # Додайте це
    "https://*.mapbox.com",    # Додано
    "https://api.mapbox.com"   # Додано
)
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
    "https://fonts.googleapis.com",
    "https://maps.googleapis.com",
    "https://*.google.com",
    "https://cdn.jsdelivr.net",
    "https://*.jsdelivr.net",
    "https://api.mapbox.com",  # Додано
    "https://*.mapbox.com"     # Додано
)
CSP_FONT_SRC = (
    "'self'",
    "data:",
    "https:",
)

ROOT_URLCONF = 'logistics_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[
            BASE_DIR / 'templates',
            BASE_DIR / 'logistics_system' / 'templates',
            BASE_DIR / 'routes' / 'templates',
            BASE_DIR / 'orders' / 'templates',
            BASE_DIR / 'users' / 'templates',
            BASE_DIR / 'telegram_bot' / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'logistics_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL = 'login' 
LOGIN_REDIRECT_URL = '/' 
LOGOUT_REDIRECT_URL = '/'  
AUTH_USER_MODEL = 'users.CustomUser' 

# GOOGLE_MAPS_API_KEY = 'AIzaSyABC7deHCmQO5p-62DciZhICHzSCwjUxDM'  # Перевірте що ключ активний
# MAPBOX_TOKEN = 'pk.eyJ1IjoibWV0Z2hvc3QiLCJhIjoiY203bHpiYnoyMGY0bTJrczZseXM1MHFzaSJ9.rWDXo6GsQmBgMBsmMhagiw'  # Перевірте що ключ активнийpython manage.py makemigrations
