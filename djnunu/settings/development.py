from .base import *

################################
##     BASE CONFIGURATION     ##
################################

DEBUG = int(os.environ.get('DEBUG', default=0))

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

################################
##      WSGI CONFIGURATION    ##
################################

WSGI_APPLICATION = 'djnunu.wsgi.application'

################################
##    DATABASE CONFIGURATION  ##
################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': config('SQL_ENGINE'),
#         'NAME': config('SQL_DATABASE'),
#         'USER': config('SQL_USER'),
#         'PASSWORD': config('SQL_PASSWORD'),
#         'HOST': config('SQL_HOST'),
#         'PORT': config('SQL_PORT'),
#     }
# }