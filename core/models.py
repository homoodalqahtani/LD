from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import RegexValidator
from django.utils.text import slugify


# ==================================================
# المستخدم المخصص
# ==================================================
class User(AbstractUser):
    """
    نموذج المستخدم المخصص لموقع رفاهية التصاميم للمقاولات
    """

    phone = models.CharField(
        "رقم الجوال",
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{9,15}$',
                message="أدخل رقم جوال صحيح"
            )
        ]
    )

    # إعادة تعريف العلاقات لتفادي تعارضات Django
    groups = models.ManyToManyField(
        Group,
        related_name="core_users",
        blank=True,
        verbose_name="المجموعات"
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="core_users_permissions",
        blank=True,
        verbose_name="الصلاحيات"
    )

    class Meta:
        verbose_name = "مستخدم"
        verbose_name_plural = "المستخدمون"

    def __str__(self) -> str:
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
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.city} – {self.district}"


# ==================================================
# إعدادات الموقع العامة (Singleton)
# ==================================================
class SiteSetting(models.Model):
    """
    إعدادات عامة للموقع (سجل واحد فقط)
    """

    site_name = models.CharField(
        "اسم الموقع",
        max_length=255,
        default="رفاهية التصاميم للمقاولات"
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

    def save(self, *args, **kwargs):
        # ضمان وجود سجل واحد فقط
        if not self.pk and SiteSetting.objects.exists():
            raise ValueError("لا يمكن إنشاء أكثر من إعداد واحد للموقع")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.site_name


# ==================================================
# الخدمات المعروضة في الصفحة الرئيسية
# ==================================================
class Service(models.Model):
    """
    خدمات رفاهية التصاميم المعروضة في الصفحة الرئيسية
    """

    title = models.CharField(
        "اسم الخدمة",
        max_length=200
    )

    slug = models.SlugField(
        "الرابط",
        max_length=220,
        unique=True,
        blank=True
    )

    description = models.TextField(
        "وصف مختصر"
    )

    icon = models.CharField(
        "أيقونة (FontAwesome)",
        max_length=100,
        blank=True,
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

    updated_at = models.DateTimeField(
        "آخر تحديث",
        auto_now=True
    )

    class Meta:
        verbose_name = "خدمة"
        verbose_name_plural = "الخدمات"
        ordering = ("order", "id")
        indexes = [
            models.Index(fields=["is_active", "order"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
