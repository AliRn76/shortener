import os
import re
from pathlib import Path
from urllib.parse import urlparse

from django.core.management import utils


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = utils.get_random_secret_key()
ALLOWED_HOSTS = ['*']
DEBUG = False

SHORTENER_URL = os.environ.get('BASE_URL', 'http://127.0.0.1:8000').strip().lower()
SHORTENER_URL.removesuffix('/')  # ex: https://url.AliRn.ir

BASE_URL = urlparse(SHORTENER_URL).hostname.split('.')[-2:]  # ex: [AliRn, ir]
BASE_URL = '.'.join(BASE_URL)  # AliRn.ir

TITLE = os.environ.get('TITLE', 'URL Shortener')
DESCRIPTION = os.environ.get('DESCRIPTION', 'Create Short & Memorable URL In a Seconds.')
PRIVATE = True if os.environ.get('PRIVATE') in ['true', 'True', '1'] else False


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'app',
]

ROOT_URLCONF = 'config.urls'

REST_FRAMEWORK = {'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer']}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (BASE_DIR / 'templates',)
    }
]

WSGI_APPLICATION = 'config.wsgi.application'

DB_DIR = BASE_DIR / 'database'
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DB_DIR / 'db.sqlite3',
    }
}
