import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# with open('./secret_key.txt') as f:
#     SECRET_KEY = f.read().strip()
# SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
if open('./secret_key.txt') is True:
    with open('./secret_key.txt') as f:
        SECRET_KEY = f.read().strip()
else:
    SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = bool(int(os.environ.get('DJANGO_DEBUG', 1)))

SECURE_SSL_REDIRECT = bool(int(os.environ.get('SECURE_SSL_REDIRECT', 0)))

ALLOWED_HOSTS = [
    'markmiloslavicjr-portfolio.herokuapp.com',
    'www.miloslavicjr.com',
    'localhost',
    '127.0.0.1'
]

PREREQ_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

PROJECT_APPS = [
    'portfolio',
    'blog',
    'markmiloslavicjr',
    'schedule',
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'markmiloslavicjr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["markmiloslavicjr/templates/"],
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

WSGI_APPLICATION = 'markmiloslavicjr.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default="sqlite:///%s" % os.path.join(BASE_DIR, 'db.sqlite3'))
}

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'markmiloslavicjr',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}
"""

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# reference url for browser to access files over http
STATIC_URL = '/static/'

# reference url for browser to access user files over http
MEDIA_URL = '/media/'

# path to store items (This is the directory that you should serve static files from in production.)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')

# path to store user items
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')
