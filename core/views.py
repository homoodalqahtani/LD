from django.shortcuts import render


# ==================================
# الصفحة الرئيسية
# ==================================
def home_view(request):
    """
    عرض الصفحة الرئيسية لموقع رفاهية التصاميم للمقاولات
    """
    context = {
        "page_title": "رفاهية التصاميم للمقاولات",
    }
    return render(request, "home.html", context)
