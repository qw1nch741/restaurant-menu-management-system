from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

# This keeps it working for local tests even when DEBUG is False
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "restaurant-menu-management-system-cyhq.onrender.com",
]


if not DEBUG:
    # (W008) Redirect all HTTP to HTTPS
    SECURE_SSL_REDIRECT = True
    # (W012) Session cookies only over HTTPS
    SESSION_COOKIE_SECURE = True
    # (W016) CSRF cookies only over HTTPS
    CSRF_COOKIE_SECURE = True
    # (W004) HSTS (Tells browser to only use HTTPS for this site)
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': int(os.environ['POSTGRES_DB_PORT']),
    }
}
