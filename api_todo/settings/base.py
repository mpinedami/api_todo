# SETUP


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# DJANGO CORE SETTINGS


ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


DEBUG = True


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INSTALLED_APPS_FIRST_PARTY = [
    "apps.todos",
]


INSTALLED_APPS_THIRD_PARTY = [
    "debug_toolbar",
    "django_linear_migrations",
    "rest_framework",
    "corsheaders",
    "whitenoise.runserver_nostatic",
]


INSTALLED_APPS_CONTRIB = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
]


INSTALLED_APPS = (
    INSTALLED_APPS_FIRST_PARTY + INSTALLED_APPS_THIRD_PARTY + INSTALLED_APPS_CONTRIB
)


INTERNAL_IPS = ["127.0.0.1"]


LANGUAGE_CODE = "en-us"


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Third party
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]


ROOT_URLCONF = "api_todo.urls"


SECRET_KEY = "django-insecure-iiq)t3zugw##x4q(8q(m=z&(cx)2$24@2#(t@+f5i(au%!f&&c"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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


TIME_ZONE = "UTC"


USE_I18N = True


USE_TZ = True


WSGI_APPLICATION = "api_todo.wsgi.application"


# DJANGO CONTRIB SETTINGS


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
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


# PROJECT SETTINS


CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:3000",
    "https://localhost:8000",
]


CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
]  # PERMITIR FORMULARIOS SIN CSRF DESDE UN FRONTEND EN REACT, VUE O ANGULAR


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}


STATIC_URL = "static/"


STATICFILES_DIRS = [BASE_DIR / "static"]


STATIC_ROOT = BASE_DIR / "staticfiles"


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
