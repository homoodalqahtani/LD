"""
URL configuration for LD project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # =========================
    # تطبيقات المتجر
    # =========================

    # المستخدمين – الحسابات – الإعدادات العامة
    path('accounts/', include('core.urls')),

    # المنتجات – التصنيفات – العرض
    path('shop/', include('catalog.urls')),

    # السلة – الطلبات – الدفع
    path('orders/', include('orders.urls')),
]
