from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # ==================================
    # الصفحة الرئيسية والمحتوى العام
    # ==================================
    path("", include("core.urls")),


    # ==================================
    # حسابات المستخدمين
    # /accounts/login/
    # /accounts/register/
    # ==================================


    # ==================================
    # المتجر
    # /shop/
    # ==================================
    path("shop/", include("catalog.urls")),


    # ==================================
    # الطلبات
    # /orders/
    # ==================================
    path("orders/", include("orders.urls")),


    # ==================================
    # لوحة التحكم (Admin)
    # ==================================
    path("admin/", admin.site.urls),
]


# ==================================
# ملفات الوسائط أثناء التطوير فقط
# ==================================
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
