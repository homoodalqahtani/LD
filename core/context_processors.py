from .models import SiteSetting, Service


def site_settings(request):
    """
    تمرير إعدادات الموقع (الاسم – الشعار) لكل القوالب
    """
    setting = SiteSetting.objects.first()
    return {
        "site": setting
    }


def active_services(request):
    """
    تمرير الخدمات المفعلة للواجهة
    """
    services = Service.objects.filter(is_active=True)
    return {
        "services": services
    }
