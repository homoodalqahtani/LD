"""
URL configuration for LD project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include

# إدارة ملفات media أثناء التطوير
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # ==================================
    # الصفحة الرئيسية
    # ==================================
    path('', include('core.urls')),


    # ==================================
    # لوحة التحكم
    # ==================================
    path('admin/', admin.site.urls),


    # ==================================
    # تطبيقات المشروع
    # ==================================

    # المستخدمين – الحسابات – الإعدادات العامة
    path('accounts/', include('core.urls')),

    # المنتجات – التصنيفات – العرض
    path('shop/', include('catalog.urls')),

    # السلة – الطلبات – الدفع
    path('orders/', include('orders.urls')),
]


# ==================================
# خدمة ملفات Media أثناء التطوير فقط
# ==================================
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
