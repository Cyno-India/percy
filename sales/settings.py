"""
Django settings for sales project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3(_bcaze(2f4-y%vb@!x_26_g12q$=wk*(%%4(+qaii&(o0*ld'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['percyweb.herokuapp.com','127.0.0.1','rocky-scrubland-84049.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #apps
    'rest_framework',
    'corsheaders',
    'user',
    'catalog',
    'customer',
    'django_filters',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',                                     # new
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sales.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sales.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.sqlite3',
#     #     'NAME': BASE_DIR / 'db.sqlite3',
#     # },
#     "default": {
#         "ENGINE": "djongo",
#         "NAME": os.environ.get('MONGO_DB_NAME'),
#         "CLIENT": {
#             "host": os.environ.get('MONGO_DB_HOST'),
#             "port": 27107,
#             "username": os.environ.get('MONGO_DB_USERNAME'),
#             "password": os.environ.get('MONGO_DB_PASSWORD'),
            
#         },
#         'TEST': {
#             'MIRROR': 'default',
#         },
#     }
# }
# DATABASES = {
#     'default': {
#         # 'ENGINE': 'django.db.backends.sqlite3',
#         # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         'ENGINE': 'djongo',
#         'ENFORCE_SCHEMA': True,
#         'NAME': 'django_mongodb_docker',
#         'HOST': 'mongodb',
#         'PORT': 27017,
#         'USER': 'root',
#         'PASSWORD': 'mongoadmin',
#         'AUTH_SOURCE': 'admin',
#         'AUTH_MECHANISM': 'SCRAM-SHA-1',
#     }
# }

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'HOST': os.environ.get('POSTGRES_HOST'),
    #     'NAME': os.environ.get('POSTGRES_NAME'),
    #     'USER': os.environ.get('POSTGRES_USER'),
    #     'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
    #     'PORT': os.environ.get('POSTGRES_PORT', 5432),

    # },
    "default": {
        "ENGINE": "djongo",
        "NAME": os.environ.get('MONGO_DB_NAME'),
        "CLIENT": {
            "host": os.environ.get('MONGO_DB_HOST'),
            # "port": int(os.environ.get('MONGO_DB_PORT')),
            "port": 27017,
            "username": os.environ.get('MONGO_DB_USERNAME'),
            "password": os.environ.get('MONGO_DB_PASSWORD'),
        },
        'TEST': {
            'MIRROR': 'default',
        },
    }
    
}

DATABASE_ROUTERS = ['user.utils.db_routers.NonRelRouter', ]

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, '/code/static'),
# )

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "user.CustomUser"

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000',
# ]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR / 'sales/app.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
