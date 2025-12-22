from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# ==================================================
# المستخدم المخصص
# ==================================================
class User(AbstractUser):
    """
    نموذج المستخدم المخصص للموقع
    """

    phone = models.CharField(
        "رقم الجوال",
        max_length=15,
        unique=True,
        null=True,
        blank=True
    )

    # إعادة تعريف العلاقات لتفادي تعارضات Django
    groups = models.ManyToManyField(
        Group,
        related_name="core_users",
        blank=True,
        verbose_name="المجموعات",
        help_text="المجموعات التي ينتمي إليها المستخدم"
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="core_users_permissions",
        blank=True,
        verbose_name="الصلاحيات",
        help_text="الصلاحيات الخاصة بالمستخدم"
    )

    class Meta:
        verbose_name = "مستخدم"
        verbose_name_plural = "المستخدمون"

    def __str__(self):
        return self.username


# ==================================================
# عناوين المستخدم
# ==================================================
class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="addresses",
        verbose_name="المستخدم"
    )

    city = models.CharField("المدينة", max_length=100)
    district = models.CharField("الحي", max_length=100)
    street = models.CharField("الشارع", max_length=255)
    postal_code = models.CharField(
        "الرمز البريدي",
        max_length=10,
        blank=True
    )

    created_at = models.DateTimeField(
        "تاريخ الإنشاء",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "عنوان"
        verbose_name_plural = "العناوين"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.city} – {self.district}"


# ==================================================
# إعدادات الموقع العامة (Singleton)
# ==================================================
class SiteSetting(models.Model):
    site_name = models.CharField(
        "اسم الموقع",
        max_length=255
    )

    site_slogan = models.CharField(
        "الشعار النصي",
        max_length=255,
        blank=True
    )

    currency = models.CharField(
        "العملة",
        max_length=10,
        default="SAR"
    )

    tax_percentage = models.DecimalField(
        "نسبة الضريبة (%)",
        max_digits=5,
        decimal_places=2,
        default=15
    )

    updated_at = models.DateTimeField(
        "آخر تحديث",
        auto_now=True
    )

    class Meta:
        verbose_name = "إعدادات الموقع"
        verbose_name_plural = "إعدادات الموقع"

    def __str__(self):
        return self.site_name


# ==================================================
# الخدمات المعروضة في الصفحة الرئيسية
# ==================================================
class Service(models.Model):
    title = models.CharField(
        "اسم الخدمة",
        max_length=200
    )

    description = models.TextField(
        "وصف مختصر"
    )

    icon = models.CharField(
        "أيقونة (FontAwesome)",
        max_length=100,
        help_text="مثال: fa-solid fa-building"
    )

    is_active = models.BooleanField(
        "مفعلة",
        default=True
    )

    order = models.PositiveIntegerField(
        "الترتيب",
        default=0
    )

    created_at = models.DateTimeField(
        "تاريخ الإنشاء",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "خدمة"
        verbose_name_plural = "الخدمات"
        ordering = ["order"]

    def __str__(self):
        return self.title
