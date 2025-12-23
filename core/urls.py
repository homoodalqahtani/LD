from django.urls import path
from . import views

# ==================================================
# Namespace لتطبيق core
# الصفحات العامة + حسابات المستخدمين
# ==================================================
app_name = "core"


urlpatterns = [

    # ==================================================
    # ================= الصفحات العامة =================
    # ==================================================

    # الصفحة الرئيسية
    # URL: /
    path(
        "",
        views.home_view,
        name="home",
    ),

    # من نحن
    # URL: /about/
    path(
        "about/",
        views.about_view,
        name="about",
    ),

    # الخدمات
    # URL: /services/
    path(
        "services/",
        views.services_view,
        name="services",
    ),

    # المشاريع (Portfolio)
    # URL: /projects/
    path(
        "projects/",
        views.projects_view,
        name="projects",
    ),

    # تواصل معنا
    # URL: /contact/
    path(
        "contact/",
        views.contact_view,
        name="contact",
    ),

    # ==================================================
    # ================= الحسابات =================
    # ==================================================

    # تسجيل الدخول
    # URL: /login/
    path(
        "login/",
        views.login_view,
        name="login",
    ),

    # إنشاء حساب
    # URL: /register/
    path(
        "register/",
        views.register_view,
        name="register",
    ),

    # الملف الشخصي
    # URL: /profile/
    path(
        "profile/",
        views.profile_view,
        name="profile",
    ),

    # تسجيل الخروج
    # URL: /logout/
    path(
        "logout/",
        views.logout_view,
        name="logout",
    ),

    # ==================================================
    # ============== إضافات مستقبلية (جاهزة) ==========
    # ==================================================

    # لوحة المستخدم (Dashboard)
    # URL: /dashboard/
    path(
        "dashboard/",
        views.profile_view,
        name="dashboard",
    ),

]
