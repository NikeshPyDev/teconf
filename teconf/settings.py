"""
Django settings for teconf project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dotenv
from django.core.exceptions import ImproperlyConfigured

DOTENV_FILE_DEFAULT = '/opt/teconf_project/.teconf.env'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv.load_dotenv(os.environ.get('DOTENV', DOTENV_FILE_DEFAULT))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ef_h_l*j)j3j_)ml$+z7e%bsl6tq#06vda*khwzta($f-6@!^z'

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
    'social_django',
    'django_forms_bootstrap',
    'tinymce',
    'proposals'
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

ROOT_URLCONF = 'teconf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'teconf.wsgi.application'

DJANGO_WYSIWYG_FLAVOR = "tinymce"
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


def get_env_var(key, default=None):
    try:
        return os.environ[key]
    except KeyError:
        if default:
            return default
        error = "Missing the '{}' environment variable!".format(key)
        raise ImproperlyConfigured(error)


DB_NAME = get_env_var('DB_NAME')
DB_USER_NAME = get_env_var('DB_USER_NAME')
DB_PASSWORD = get_env_var('DB_PASSWORD')
DB_HOST = get_env_var('DB_HOST')
DB_PORT = get_env_var('DB_PORT')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": DB_NAME,
        "USER": DB_USER_NAME,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
        # "CONN_MAX_AGE": 300,
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "teconf",
#         "USER": "teconf",
#         "PASSWORD": "teconf",
#         "HOST": "localhost",
#         "PORT": 5432,
#         # "CONN_MAX_AGE": 300,
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'teconf', 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'teconf', 'static'),
)


AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'social_core.backends.github.GithubOAuth2',  # for Github authentication
    'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication

    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = get_env_var('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')  # Paste CLient Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = get_env_var('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')  # Paste Secret Key

SOCIAL_AUTH_GITHUB_KEY = get_env_var('SOCIAL_AUTH_GITHUB_KEY')  # Paste Client ID
SOCIAL_AUTH_GITHUB_SECRET = get_env_var('SOCIAL_AUTH_GITHUB_SECRET')  # Paste Secret Key

EMAIL_BACKEND = get_env_var('EMAIL_BACKEND')
EMAIL_HOST = get_env_var('EMAIL_HOST')
EMAIL_PORT = get_env_var('EMAIL_PORT')
EMAIL_HOST_USER = get_env_var('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_var('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = get_env_var('DEFAULT_FROM_EMAIL')

LOGIN_REDIRECT_URL = "/proposals/"
