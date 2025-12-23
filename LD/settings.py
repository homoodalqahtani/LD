from pathlib import Path
import os


# ==================================================
# المسار الأساسي للمشروع
# ==================================================
BASE_DIR = Path(__file__).resolve().parent.parent


# ==================================================
# مجلد القوالب الرئيسي
# ==================================================
TEMPLATES_DIR = BASE_DIR / "templates"


# ==================================================
# الأمان (Security)
# ==================================================
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-change-this-in-production"
)

DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# ==================================================
# التطبيقات
# ==================================================
INSTALLED_APPS = [

    # Django Core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Local Apps
    "core.apps.CoreConfig",
    "catalog.apps.CatalogConfig",
    "orders.apps.OrdersConfig",
]


# ==================================================
# المستخدم المخصص
# ==================================================
AUTH_USER_MODEL = "core.User"


# ==================================================
# إعدادات تسجيل الدخول
# ==================================================
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


# ==================================================
# الوسائط (Middleware)
# ==================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==================================================
# إعدادات الروابط
# ==================================================
ROOT_URLCONF = "LD.urls"


# ==================================================
# القوالب (Templates)
# ==================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [TEMPLATES_DIR],

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


# ==================================================
# WSGI
# ==================================================
WSGI_APPLICATION = "LD.wsgi.application"


# ==================================================
# قاعدة البيانات
# ==================================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ==================================================
# التحقق من كلمات المرور
# ==================================================
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 8},
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ==================================================
# اللغة والتوقيت (🇸🇦)
# ==================================================
LANGUAGE_CODE = "ar"
TIME_ZONE = "Asia/Riyadh"

USE_I18N = True
USE_TZ = True


# ==================================================
# اللغات + RTL
# ==================================================
LANGUAGES = [
    ("ar", "العربية"),
]

LOCALE_PATHS = [
    BASE_DIR / "locale",
]


# ==================================================
# تخصيص لوحة التحكم (Admin Branding)
# ==================================================
ADMIN_SITE_HEADER = "رفاهية التصاميم – لوحة التحكم"
ADMIN_SITE_TITLE = "رفاهية التصاميم"
ADMIN_INDEX_TITLE = "إدارة الموقع"


# ==================================================
# الملفات الثابتة (Static)  ✅ (مهم)
# ==================================================
STATIC_URL = "/static/"

# مجلد static أثناء التطوير
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# مجلد التجميع للإنتاج
STATIC_ROOT = BASE_DIR / "staticfiles"


# ==================================================
# ملفات الوسائط (Media)
# ==================================================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ==================================================
# الجلسات (Sessions)
# ==================================================
SESSION_COOKIE_AGE = 60 * 60 * 24  # 24 ساعة
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False


# ==================================================
# إعدادات الأمان
# ==================================================
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = "DENY"


# ==================================================
# HTTPS (يُفعّل تلقائيًا في الإنتاج فقط)
# ==================================================
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
else:
    SECURE_SSL_REDIRECT = False


# ==================================================
# الإعدادات الافتراضية
# ==================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
