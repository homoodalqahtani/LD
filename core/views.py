from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

User = get_user_model()


# ==================================================
# الصفحة الرئيسية
# ==================================================
def home_view(request):
    return render(request, "core/home.html")


# ==================================================
# الصفحات العامة
# ==================================================
def about_view(request):
    return render(request, "core/about.html")


def services_view(request):
    context = {
        "breadcrumb": [
            {"title": "خدماتنا"},
        ]
    }
    return render(request, "core/services.html", context)


def projects_view(request):
    context = {
        "breadcrumb": [
            {"title": "أعمالنا"},
        ]
    }
    return render(request, "core/projects.html", context)


def contact_view(request):
    return render(request, "core/contact.html")


# ==================================================
# إنشاء حساب
# ==================================================
@require_http_methods(["GET", "POST"])
def register_view(request):
    if request.user.is_authenticated:
        return redirect("core:home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        phone = request.POST.get("phone", "").strip()
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not username or not password1 or not password2:
            messages.error(request, "جميع الحقول مطلوبة")
            return redirect("core:register")

        if password1 != password2:
            messages.error(request, "كلمتا المرور غير متطابقتين")
            return redirect("core:register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم مسبقًا")
            return redirect("core:register")

        user = User.objects.create_user(
            username=username,
            password=password1
        )

        if phone:
            user.phone = phone
            user.save(update_fields=["phone"])

        login(request, user)
        messages.success(request, "تم إنشاء الحساب بنجاح")

        return redirect("core:home")

    return render(request, "core/register.html")


# ==================================================
# تسجيل الدخول
# ==================================================
@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "يرجى إدخال البيانات")
            return redirect("core:login")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول")
            return redirect("core:home")

        messages.error(request, "بيانات الدخول غير صحيحة")

    return render(request, "core/login.html")


# ==================================================
# تسجيل الخروج
# ==================================================
@login_required(login_url="core:login")
def logout_view(request):
    logout(request)
    messages.info(request, "تم تسجيل الخروج")
    return redirect("core:home")


# ==================================================
# الملف الشخصي
# ==================================================
@login_required(login_url="core:login")
def profile_view(request):
    return render(request, "core/profile.html")
