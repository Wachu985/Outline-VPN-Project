from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USSER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST':'127.0.0.1',
        'PORT':'5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR/'static/']

"""Configurando la URL con que van a salir los Archivos Media"""
MEDIA_URL = '/media/'

"""Configurando la direccion de la Carpeta Media"""
MEDIA_ROOT = BASE_DIR/'media'

"""Configurando CKEDITOR"""
CKEDITOR_UPLOAD_PATH =  'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js'

#Configuracion del CKEDITOR
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':'Custom',
        'toolbar_Custom': [
            ['Bold','Italic','Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-','JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl','Language'],
            ['TextColor','Format','FrontSize','Link'],
            ['Smiley','Image','Iframe'],
            ['RemoveFormat','Source']
        ],
        'stylesSet':[
            
        ]
    }
}

#EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = get_secret('EMAIL_USER')
EMAIL_HOST_PASSWORD = get_secret('EMAIL_PASSWORD')
