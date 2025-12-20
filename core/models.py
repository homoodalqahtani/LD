from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User Model
    قابل للتوسعة لاحقًا (جوال – تحقق – صلاحيات)
    """
    phone = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        verbose_name="رقم الجوال"
    )

    def __str__(self):
        return self.username


class Address(models.Model):
    """
    عناوين المستخدم (شحن / فواتير)
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses'
    )
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.district}"


class SiteSetting(models.Model):
    """
    إعدادات المتجر العامة
    """
    site_name = models.CharField(max_length=255)
    currency = models.CharField(max_length=10, default='SAR')
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=15)

    def __str__(self):
        return self.site_name
