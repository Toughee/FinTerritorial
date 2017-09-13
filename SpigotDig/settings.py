import os
import socket
if socket.gethostname()=="COMPSYSTEM": 
    from local_settings import *

##########################################################################################

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

##########################################################################################

#SECRET_KEY = '=(n^v8a8ni%ht_w=uc=b*0hlf8v^0)4tox^o_ovuhmq4vl7%0a'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '=n^v8a8ni%ht_w=uc=b*0hlf8v^0)4tox^o_ovuhmq4vl7%0a')

##########################################################################################

DEBUG = bool( os.environ.get('DJANGO_DEBUG', True))

##########################################################################################


#### Security Settings ####

##########################################################################################

SECURE_CONTENT_TYPE_NOSNIFF = True

##########################################################################################

SESSION_COOKIE_SECURE = True

##########################################################################################

SECURE_BROWSER_XSS_FILTER = True

##########################################################################################

#sends it into a https connection. Making the app incompatible 
    #SECURE_SSL_REDIRECT = True

CSRF_COOKIE_SECURE = True

##########################################################################################

CSRF_COOKIE_HTTPONLY = True

##########################################################################################

X_FRAME_OPTIONS = 'DENY'

##########################################################################################

SECURE_HSTS_SECONDS = 31536000

##########################################################################################

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

##########################################################################################


ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'www.SpigotDig.com']

ADMINS  = [( 'T.Jim', 'Marotjimenez@gmail.com')]


###########################################################################################

#### Application definitions ####

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stateselect',
]

##########################################################################################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

##########################################################################################

ROOT_URLCONF = 'SpigotDig.urls'

##########################################################################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

##########################################################################################

WSGI_APPLICATION = 'SpigotDig.wsgi.application'

##########################################################################################


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

##########################################################################################

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

##########################################################################################

LANGUAGE_CODE = 'en-us'

##########################################################################################

TIME_ZONE = 'UTC'

##########################################################################################

USE_I18N = True

##########################################################################################

USE_L10N = True

##########################################################################################

USE_TZ = True

##########################################################################################

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

##########################################################################################

MEDIA_URL = '/media/'

##########################################################################################

STATIC_ROOT = os.path.join(BASE_DIR, 'stateselect', 'static')

##########################################################################################

STATIC_URL = '/static/'

##########################################################################################

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

##########################################################################################

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

##########################################################################################