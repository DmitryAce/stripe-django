from .base import *
from .utils import get_unfold_config

DEBUG = True

# Для разработки — SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}