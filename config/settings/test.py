"""
Test settings for aircnc_clone project.
"""

from .base import *

# Debug mode for tests
DEBUG = True

# Test database - In-memory SQLite for speed
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'OPTIONS': {
            'timeout': 20,
        }
    }
}

# Disable migrations for faster tests
class DisableMigrations:
    def __contains__(self, item):
        return True
    
    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()

# Use dummy cache for tests
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    'sessions': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Use dummy session backend for tests
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Email backend for tests
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Password hashers - Use fast hasher for tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Celery - Execute tasks synchronously in tests
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# Logging - Minimal logging for tests
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',  # Only show warnings and errors
    },
}

# Media files - Use temporary directory for tests
import tempfile
MEDIA_ROOT = tempfile.mkdtemp()

# Static files - Disable static file collection for tests
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
