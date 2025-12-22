from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

User = get_user_model()


# ==================================================
# الصفحة الرئيسية (Landing Page)
# ==================================================
def home_view(request):
    """
    الصفحة الرئيسية لموقع رفاهية التصاميم
    """
    context = {
        "page_title": "رفاهية التصاميم للمقاولات",
    }
    return render(request, "home.html", context)


# ==================================================
# إنشاء حساب
# ==================================================
@require_http_methods(["GET", "POST"])
def register_view(request):
    """
    إنشاء حساب مستخدم جديد
    """
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        phone = request.POST.get("phone", "").strip()
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # تحقق من المدخلات
        if not username or not password1 or not password2:
            messages.error(request, "جميع الحقول مطلوبة")
            return redirect("accounts:register")

        if password1 != password2:
            messages.error(request, "كلمتا المرور غير متطابقتين")
            return redirect("accounts:register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم مسبقًا")
            return redirect("accounts:register")

        # إنشاء المستخدم
        user = User.objects.create_user(
            username=username,
            phone=phone,
            password=password1
        )

        login(request, user)
        messages.success(request, "تم إنشاء الحساب وتسجيل الدخول بنجاح")

        return redirect("home")

    return render(request, "core/register.html")


# ==================================================
# تسجيل الدخول
# ==================================================
@require_http_methods(["GET", "POST"])
def login_view(request):
    """
    تسجيل دخول المستخدم
    """
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "يرجى إدخال اسم المستخدم وكلمة المرور")
            return redirect("accounts:login")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح")
            return redirect("home")

        messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة")

    return render(request, "core/login.html")


# ==================================================
# تسجيل الخروج
# ==================================================
@login_required(login_url="accounts:login")
def logout_view(request):
    """
    تسجيل خروج المستخدم
    """
    logout(request)
    messages.info(request, "تم تسجيل الخروج بنجاح")
    return redirect("home")


# ==================================================
# الملف الشخصي
# ==================================================
@login_required(login_url="accounts:login")
def profile_view(request):
    """
    صفحة الملف الشخصي
    """
    context = {
        "user": request.user,
    }
    return render(request, "core/profile.html", context)
