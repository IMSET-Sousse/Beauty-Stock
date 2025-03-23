from pathlib import Path
import os  # Il faut importer os pour les chemins relatifs

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ts9o%p5(a#&$svw##ko#t(jl)@h1lpq9=-4)g#k#a)t3g1gt-f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []  # Ajouter les hôtes autorisés en production, exemple: ['localhost', 'example.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'produits',  # Assurez-vous que 'produits' est bien ajouté ici
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'app.urls'

# Templates settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Vérifiez que 'templates' est bien inclus ici
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Utilisation du Path() pour spécifier le chemin
    }
}

# Password validation settings
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'  # Utilisez 'fr-fr' pour le français si nécessaire
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Fichiers statiques supplémentaires
STATICFILES_DIRS = [
    BASE_DIR / 'produits/static',  # Répertoire des fichiers statiques spécifiques à l'application
]

# Configure l'emplacement où les fichiers statiques seront collectés (en production uniquement)
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Pour la production uniquement (lors du déploiement)

# Fichier CSS statique principal
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Login URL
LOGIN_URL = 'connexion'  # Redirection vers la page de connexion si l'utilisateur n'est pas connecté

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
