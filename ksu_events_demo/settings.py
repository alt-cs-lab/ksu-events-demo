"""
Django settings for ksu_events_demo project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from os import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

EVENTS_TEMPLATES_DIR = Path(
    BASE_DIR.parent, "ksu-events/ksu_events/base/templates")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ng9r$dniojrs6(ogltcrt(y64n-@d5v!c2o1(r28conrk0b#-7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ksu_events',
    'ksu_events.registration',
    'django_ksu_cas_auth',
    'ksu_events_demo',
    'django_cas_ng',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# implementation configuration
CAS_SERVER_URL = 'https://signin.k-state.edu/WebISO/'
useTestCas = False  # set true to use testcas.cs.ksu.edu

# cas logic

if environ.get('CODESPACES') is None:
    CAS_REDIRECT_URL = '/'
else:
    useTestCas = True  # set false to use other cas with codespaces
    CODESPACE_NAME = environ['CODESPACE_NAME']
    CAS_REDIRECT_URL = f'https://{CODESPACE_NAME}-8000.app.github.dev/'
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    USE_X_FORWARDED_HOST = True
    USE_X_FORWARDED_PORT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    ALLOWED_HOSTS = [f'{CODESPACE_NAME}-8000.app.github.dev']
if useTestCas:
    CAS_SERVER_URL = 'https://testcas.cs.ksu.edu'
    MIDDLEWARE.insert(
        0, 'ksu_events_demo.middleware.FixTestCASRedirectMiddleware')

CAS_LOGOUT_COMPLETELY = False
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
AUTH_USER_MODEL = 'ksu_events.User'

ROOT_URLCONF = 'ksu_events_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # EVENTS_TEMPLATES_DIR
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

WSGI_APPLICATION = 'ksu_events_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres" if environ.get('DB_NAME') is None else environ.get('DB_NAME'),
        "USER": "postgres" if environ.get('DB_USER') is None else environ.get('DB_USER'),
        "PASSWORD": "postgres" if environ.get('DB_PASSWORD') is None else environ.get('DB_PASSWORD'),
        "HOST": "127.0.0.1" if environ.get('DB_HOST') is None else environ.get('DB_HOST'),
        "PORT": "5432" if environ.get('DB_PORT') is None else environ.get('DB_PORT'),
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

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
