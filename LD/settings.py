from pathlib import Path


# ==================================================
# المسار الأساسي للمشروع
# ==================================================
BASE_DIR = Path(__file__).resolve().parent.parent


# ==================================================
# مجلد القوالب الرئيسي
# ==================================================
TEMPLATES_DIR = BASE_DIR / 'templates'


# ==================================================
# الأمان (Security)
# ==================================================
SECRET_KEY = 'django-insecure-change-this-in-production'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# ==================================================
# التطبيقات
# ==================================================
INSTALLED_APPS = [
    # Django Core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local Apps
    'core.apps.CoreConfig',
    'catalog.apps.CatalogConfig',
    'orders.apps.OrdersConfig',
]


# ==================================================
# المستخدم المخصص
# ==================================================
AUTH_USER_MODEL = 'core.User'


# ==================================================
# الوسائط (Middleware)
# ==================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==================================================
# إعدادات الروابط
# ==================================================
ROOT_URLCONF = 'LD.urls'


# ==================================================
# القوالب (Templates)
# ==================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # مجلد templates الرئيسي
        'DIRS': [TEMPLATES_DIR],

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


# ==================================================
# WSGI
# ==================================================
WSGI_APPLICATION = 'LD.wsgi.application'


# ==================================================
# قاعدة البيانات
# ==================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==================================================
# التحقق من كلمات المرور
# ==================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8},
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ==================================================
# اللغة والتوقيت (🇸🇦)
# ==================================================
LANGUAGE_CODE = 'ar'

TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_TZ = True


# ==================================================
# اللغات + RTL
# ==================================================
LANGUAGES = [
    ('ar', 'العربية'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


# ==================================================
# الملفات الثابتة (Static)
# ==================================================
STATIC_URL = '/static/'

# ملفات التصميم أثناء التطوير
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# مجلد التجميع للإنتاج
STATIC_ROOT = BASE_DIR / 'staticfiles'


# ==================================================
# ملفات الوسائط (Media)
# ==================================================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ==================================================
# الإعدادات الافتراضية
# ==================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
