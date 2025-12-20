from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    """
    المستخدم المخصص
    """

    phone = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        verbose_name="رقم الجوال"
    )

    groups = models.ManyToManyField(
        Group,
        related_name='core_users',
        blank=True,
        verbose_name="المجموعات",
        help_text="المجموعات التي ينتمي إليها المستخدم"
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='core_users_permissions',
        blank=True,
        verbose_name="الصلاحيات",
        help_text="الصلاحيات الخاصة بالمستخدم"
    )

    class Meta:
        verbose_name = "مستخدم"
        verbose_name_plural = "المستخدمون"

    def __str__(self):
        return self.username


class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses',
        verbose_name="المستخدم"
    )
    city = models.CharField(max_length=100, verbose_name="المدينة")
    district = models.CharField(max_length=100, verbose_name="الحي")
    street = models.CharField(max_length=255, verbose_name="الشارع")
    postal_code = models.CharField(
        max_length=10,
        blank=True,
        verbose_name="الرمز البريدي"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء"
    )

    class Meta:
        verbose_name = "عنوان"
        verbose_name_plural = "العناوين"

    def __str__(self):
        return f"{self.city} - {self.district}"


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=255, verbose_name="اسم المتجر")
    currency = models.CharField(max_length=10, default='SAR', verbose_name="العملة")
    tax_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=15,
        verbose_name="نسبة الضريبة (%)"
    )

    class Meta:
        verbose_name = "إعدادات المتجر"
        verbose_name_plural = "إعدادات المتجر"

    def __str__(self):
        return self.site_name
