"""
Django settings for test_site project.

Generated by 'django-admin startproject' using Django 2.2.28.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os, sys
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


if "runserver" in sys.argv:
    DEBUG = True
    PREPEND_WWW = False
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    CORS_ORIGIN_ALLOW_ALL = True
else:
    DEBUG = False
    PREPEND_WWW = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:8000",  # Add your domain(s) here
    ]
CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "https://datasadvocate.dev",
    "http://datasadvocate.dev",
]

# DIRNAME = os.path.abspath(os.path.dirname(__file__))
# This file will return a local directory.
# e.g: '/home/pi/Documents/Django_files/djenv/test_site/test_site'
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = "/sound/"

# This file will return a base directory.
# e.g: '/home/pi/Documents/Django_files/djenv/test_site'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("secret_key_website")

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = [
    "*",
    "*.datasadvocate.dev",
]
# Default settings

BOOTSTRAP5 = {
    # The complete URL to the Bootstrap CSS file
    # Note that a URL can be either a string,
    # e.g. "https://stackpath.bootstrapcdn.com/bootstrap/5.1.1/css/bootstrap.min.css",
    # or a dict like the default value below.
    "css_url": {
        "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css",
        "integrity": "sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65",
        "crossorigin": "anonymous",
    },
    # The complete URL to the Bootstrap JavaScript file
    "javascript_url": {
        "url": "https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js",
        "integrity": "sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4",
        "crossorigin": "anonymous",
    },
    # The complete URL to the Bootstrap CSS file (None means no theme)
    "theme_url": None,
    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap5.html)
    "javascript_in_head": False,
    # Label class to use in horizontal forms
    "horizontal_label_class": "col-md-3",
    # Field class to use in horizontal forms
    "horizontal_field_class": "col-md-9",
    # Set placeholder attributes to label if no placeholder is provided
    "set_placeholder": True,
    # Class to indicate required (better to set this in your Django form)
    "required_css_class": "",
    # Class to indicate error (better to set this in your Django form)
    "error_css_class": "is-invalid",
    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    "success_css_class": "is-valid",
    # Renderers (only set these if you have studied the source and understand the inner workings)
    "formset_renderers": {
        "default": "bootstrap5.renderers.FormsetRenderer",
    },
    "form_renderers": {
        "default": "bootstrap5.renderers.FormRenderer",
    },
    "field_renderers": {
        "default": "bootstrap5.renderers.FieldRenderer",
        "inline": "bootstrap5.renderers.InlineFieldRenderer",
    },
}

# Application definition

INSTALLED_APPS = [
    # apps
    "landing",
    "resume",
    "api",
    "examples",
    # dependency
    "sass_processor",
    "rest_framework",
    "bootstrap5",
    "csp",
    "corsheaders",
    # other stuff
    "django_user_agents",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
]


CSP_SCRIPT_SRC = [
    "'self'",
    "'unsafe-eval'",
    "'unsafe-inline'",
    "https://code.jquery.com",
    "https://ssl.gstatic.com",
    "https://cdnjs.cloudflare.com",
    "https://cdn.jsdelivr.net",
    "https://www.gstatic.com",
    "https://maps.googleapis.com",
    "https://ajax.googleapis.com",
    "https://cdn.lordicon.com",
    "https://code.iconify.design",
    "https://fonts.googleapis.com",
]
CSP_CONNECT_SRC = [
    "'self'",
    "http://127.0.0.1:8000/*",
    "'unsafe-inline'",
    "https://127.0.0.1:8000/*",
    "'unsafe-eval'",
    "https://api.themoviedb.org",
    "https://www.gstatic.com",
    "https://maps.googleapis.com",
    "https://cdn.lordicon.com",
    "https://localhost:8000",
    "https://localhost:8000",
    "https://fonts.googleapis.com"
]
CSP_DEFAULT_SRC = [
    "'self'",
    "http://127.0.0.1:8000",
    "https://127.0.0.1:8000",
    "http://127.0.0.1:8000/favicon.ico",
    "https://127.0.0.1:8000/favicon.ico",
    "'unsafe-inline'",
    "https://www.youtube.com",
    "https://trends.google.com",
    "https://cdn.jsdelivr.net",
    "https://fonts.googleapis.com",
    "https://cdnjs.cloudflare.com",
    "https://cdn.datatables.net",
    "https://www.gstatic.com",
    "https://fonts.googleapis.com"
]
CSP_IMG_SRC = [
    "'self'",
    "data:",
    "https://s3-us-west-2.amazonaws.com",
    "https://i.kym-cdn.com",
    "https://images.pexels.com",
    "https://image.tmdb.org",
    "https://fonts.googleapis.com"
]
CSP_FONT_SRC = [
    "'self'",
    "https://fonts.gstatic.com/",
    "https://cdnjs.cloudflare.com",
    "https://cdn.datatables.net",
    "https://cdn.jsdelivr.net",
    "https://fonts.googleapis.com",
    
]

ROOT_URLCONF = "rport.urls"
# to add html templates simply add the source into the DIRS array.

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "landing", "html"),
            os.path.join(BASE_DIR, "resume", "html"),
            os.path.join(BASE_DIR, "resume", "html"),
            os.path.join(BASE_DIR, "examples", "html"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "rport.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
# Note for apache: https://stackoverflow.com/questions/28716741/djangooperationalerror-at-admin-login-unable-to-open-database-file


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "sass_processor.finders.CssFinder",
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# Configuration for django-sass-processor
SASS_PROCESSOR_ENABLED = True
SASS_PROCESSOR_ROOT = STATIC_ROOT
SASS_PROCESSOR_INCLUDE_DIRS = [
    STATIC_ROOT + "scss/",  # Path to your SCSS files
]
SASS_PROCESSOR_OUTPUT_DIR = "css"
SASS_PRECISION = 8


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # "DEFAULT_PERMISSION_CLASSES": [
    #     "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    # ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}
# # https://stackoverflow.com/questions/52974549/django-rest-framework-web-login-not-working
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
#         'LOCATION': 'localhost:11211',
#     }
# }
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "django_cache",
    }
}
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = env("app_email")
EMAIL_HOST_PASSWORD = env("django_pass")
EMAIL_USE_TLS = True
EMAIL_PORT = 587

# SECURE_SSL_REDIRECT=False
# SESSION_COOKIE_SECURE=False
# CSRF_COOKIE_SECURE=False
