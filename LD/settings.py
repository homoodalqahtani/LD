from pathlib import Path

# =========================
# المسار الأساسي للمشروع
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# الأمان (Security)
# =========================
SECRET_KEY = 'django-insecure-change-this-in-production'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# =========================
# التطبيقات
# =========================
INSTALLED_APPS = [
    # Django Core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local Apps (E-Commerce Core)
    'core',       # المستخدمين – الصلاحيات – الإعدادات العامة
    'catalog',    # المنتجات – التصنيفات – المخزون
    'orders',     # السلة – الطلبات – الدفع
]


# =========================
# المستخدم المخصص (Custom User)
# =========================
AUTH_USER_MODEL = 'core.User'


# =========================
# الوسائط (Middleware)
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # الجلسات + اللغات + التوقيت
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =========================
# الإعدادات الأساسية
# =========================
ROOT_URLCONF = 'LD.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # مجلد templates الرئيسي
        'DIRS': [BASE_DIR / 'templates'],

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

WSGI_APPLICATION = 'LD.wsgi.application'


# =========================
# قاعدة البيانات
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================
# التحقق من كلمات المرور
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# =========================
# اللغة والتوقيت (🇸🇦)
# =========================
LANGUAGE_CODE = 'ar'

TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# =========================
# إعدادات الاتجاه RTL
# =========================
LANGUAGES = [
    ('ar', 'العربية'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


# =========================
# الملفات الثابتة
# =========================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# =========================
# الإعدادات الافتراضية
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
