from django.contrib import admin
from .models import User, Address, SiteSetting


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'district', 'created_at')
    list_filter = ('city',)
    search_fields = ('user__username', 'city', 'district')


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'currency', 'tax_percentage')
