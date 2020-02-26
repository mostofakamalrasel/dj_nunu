from .base import *

################################
##     BASE CONFIGURATION     ##
################################

DEBUG = int(os.environ.get('DEBUG', default=1))

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

################################
##      AUTH CONFIGURATION    ##
################################

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