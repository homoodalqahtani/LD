from django.contrib import admin
from .models import User, Address, SiteSetting


# ==================================================
# تخصيص لوحة التحكم
# ==================================================
admin.site.site_header = "رفاهية التصاميم – لوحة التحكم"
admin.site.site_title = "رفاهية التصاميم"
admin.site.index_title = "إدارة الموقع"


# ==================================================
# المستخدمين
# ==================================================
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'phone',
        'is_staff',
        'is_active',
        'date_joined',
    )

    list_filter = (
        'is_staff',
        'is_active',
    )

    search_fields = (
        'username',
        'email',
        'phone',
    )

    ordering = ('-date_joined',)

    fieldsets = (
        ('معلومات الحساب', {
            'fields': ('username', 'password'),
        }),
        ('معلومات التواصل', {
            'fields': ('email', 'phone'),
        }),
        ('الصلاحيات', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        ('معلومات النظام', {
            'fields': ('last_login', 'date_joined'),
        }),
    )

    readonly_fields = ('last_login', 'date_joined')


# ==================================================
# العناوين
# ==================================================
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'city',
        'district',
        'created_at',
    )

    list_filter = (
        'city',
        'created_at',
    )

    search_fields = (
        'user__username',
        'user__phone',
        'city',
        'district',
    )

    ordering = ('-created_at',)


# ==================================================
# إعدادات الموقع
# ==================================================
@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = (
        'site_name',
        'currency',
        'tax_percentage',
    )

    fieldsets = (
        ('الهوية', {
            'fields': ('site_name', 'logo'),
        }),
        ('الإعدادات المالية', {
            'fields': ('currency', 'tax_percentage'),
        }),
    )
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('title',)
    ordering = ('order',)
