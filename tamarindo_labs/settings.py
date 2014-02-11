import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'fg696j@d_!bud=s726*q7#=#u1@2q0t5sda6$@ff*55%^@dersbg'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = []
APPS = ["apps.website",
        "apps.admin_sas"]
try:
    import django_extensions
    APPS += ["django_extensions"]
except:
    pass
 

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
)  + tuple(APPS)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',

)

ROOT_URLCONF = 'tamarindo_labs.urls'
WSGI_APPLICATION = 'tamarindo_labs.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

try:
    from .local_settings import DATABASES
except Exception, e:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = (
    os.sep.join([os.path.dirname(os.path.dirname(__file__)), 'public/static']),
)
MEDIA_ROOT = os.sep.join([os.path.dirname(os.path.dirname(__file__)), 'public/media'])

STATIC_URL= '/static/'
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.sep.join([os.path.dirname(os.path.dirname(__file__)), 'templates']),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)