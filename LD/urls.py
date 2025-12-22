from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # ==================================
    # الصفحة الرئيسية
    # ==================================
    path('', include('core.home_urls')),


    # ==================================
    # حسابات المستخدمين
    # ==================================
    path('accounts/', include('core.urls')),


    # ==================================
    # لوحة التحكم
    # ==================================
    path('admin/', admin.site.urls),


    # ==================================
    # المتجر
    # ==================================
    path('shop/', include('catalog.urls')),


    # ==================================
    # الطلبات
    # ==================================
    path('orders/', include('orders.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
