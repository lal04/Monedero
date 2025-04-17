from .base import *

# Entorno de desarrollo
DEBUG = True
ALLOWED_HOSTS = ['*']

# Base de datos para desarrollo (por ejemplo, SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Otros posibles ajustes para desarrollo (puedes agregar más según tus necesidades)
