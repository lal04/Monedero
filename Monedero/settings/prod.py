from .base import *

# Entorno de producción
DEBUG = False
ALLOWED_HOSTS = ['raul200004.pythonanywhere.com']

# Seguridad en producción
SECURE_HSTS_SECONDS = 31536000
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Base de datos para producción (por ejemplo, PostgreSQL)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'nombre_bd',
#         'USER': 'usuario',
#         'PASSWORD': 'contraseña',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Otras configuraciones de seguridad específicas para producción
