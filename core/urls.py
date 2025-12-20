from django.urls import path
from . import views

# اسم التطبيق (مهم للتوسعة واستخدام namespace لاحقًا)
app_name = 'core'

urlpatterns = [

    # =========================
    # الصفحة الرئيسية
    # =========================
    path('', views.home_view, name='home'),

]
