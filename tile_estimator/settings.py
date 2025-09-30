

from datetime import timedelta
import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-key-for-development-only')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'  # Default to True for local development

CSRF_TRUSTED_ORIGINS = [
    "https://tilenet.onrender.com",
    "https://web-production-c1b96.up.railway.app",
    "https://healthcheck.railway.app",
    "https://*.railway.app",
    "https://*.up.railway.app",
    "https://tilneett.netlify.app",
    "https://tilnet.app",
    "https://www.tilnet.app",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
    "http://localhost:5175",
    "http://127.0.0.1:5175",
]
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
   # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',  # Added for token authentication
    'corsheaders',
    'phonenumber_field',
    
    # # Custom apps
    'accounts',
    'estimates',
    'subscriptions',
    'suppliers',
    'admin_api',
    'projects',  # Projects app
    'manual_estimate',
]
# your_project_name/settings.py
ROOT_URLCONF = 'tile_estimator.urls'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'tile_estimator.wsgi.application'

# Database configuration
# Use Railway PostgreSQL database
DATABASE_URL = "postgresql://postgres:HwdCnuWZklkEWApRIhzZjcJMHOhOCMPT@mainline.proxy.rlwy.net:30544/railway"

DATABASES = {
    "default": dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        conn_health_checks=True
    )
}
AUTH_USER_MODEL = 'accounts.CustomUser'

# Password validation
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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'accounts.authentication.SingleSessionJWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=1340),  # Short, so it forces refresh often
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),    # 2 days login duration
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}


ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "tilenet.onrender.com",
    "web-production-c1b96.up.railway.app",  # Your specific Railway domain
    "healthcheck.railway.app",  # Railway health check domain
    ".railway.app",  # All Railway domains
    ".up.railway.app",  # All Railway domains
    "tilneett.netlify.app",  # Current Netlify domain
    "tilnet.app",  # Your main domain
    "www.tilnet.app",  # WWW subdomain
]
# CORS settings
CORS_ALLOW_ALL_ORIGINS = os.environ.get('CORS_ALLOW_ALL_ORIGINS', 'False').lower() == 'true'

# For local development, allow localhost origins
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",  # Vite default port
    "http://127.0.0.1:5173",
    "http://localhost:5174",  # Additional Vite port
    "http://127.0.0.1:5174",
    "http://localhost:5175",  # Current Vite port
    "http://127.0.0.1:5175",
    "https://tilneett.netlify.app",  # Current Netlify domain
    "https://tilnet.app",  # Your main domain
    "https://www.tilnet.app",  # WWW subdomain
]

# Allow credentials to be sent with requests
CORS_ALLOW_CREDENTIALS = True
# os.getenv('AFRICASTALKING_API_KEY')
AFRICASTALKING_USERNAME = os.getenv('AFRICASTALKING_USERNAME', 'sandbox') # Keep sandbox for local
AFRICASTALKING_API_KEY = os.getenv('AFRICASTALKING_API_KEY', '') # Empty string default is safer
PAYSTACK_SECRET_KEY = os.getenv('PAYSTACK_SECRET_KEY', 'sk_test_your_secret_key_here')

PAYSTACK_PUBLIC_KEY = os.getenv('PAYSTACK_PUBLIC_KEY', '')
PAYSTACK_CALLBACK_URL = os.getenv('PAYSTACK_CALLBACK_URL', '')
VERIFICATION_CODE_EXPIRY_MINUTES = 10

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Whitenoise configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Paystack settings
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

LOGGING = {
    "version": 1,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",  # Changed to DEBUG for better logging
    },
    "loggers": {
        "django.db.backends": {
            "level": "DEBUG",
            "handlers": ["console"],
        },
    },
}

# Subscription plan settings for freemium model
SUBSCRIPTION_PLANS = {
    'free': {
        'name': 'Free',
        'max_projects': 3,
        'max_estimates_per_month': 10,
        'features': ['quick_estimates', 'basic_project_management'],
    },
    'standard': {
        'name': 'Standard',
        'price_monthly': 1500,  # in cents
        'price_yearly': 15000,  # in cents
        'max_projects': 20,
        'max_estimates_per_month': 50,
        'features': ['quick_estimates', 'detailed_project_management', 'pdf_exports', 'supplier_access'],
    },
    'premium': {
        'name': 'Premium',
        'price_monthly': 3000,  # in cents
        'price_yearly': 30000,  # in cents
        'max_projects': -1,  # unlimited
        'max_estimates_per_month': -1,  # unlimited
        'features': ['quick_estimates', 'detailed_project_management', 'pdf_exports', 'supplier_access', 
                     'advanced_analytics', 'team_access', 'api_access', 'priority_support'],
    },
}


# settings.py (at the very bottom of the file)
import logging
logger = logging.getLogger(__name__)
logger.info("Django settings loaded successfully.") # Add this line