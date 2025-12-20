from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم التصنيف")
    slug = models.SlugField(unique=True, verbose_name="الرابط")
    is_active = models.BooleanField(default=True, verbose_name="نشط")

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name="التصنيف"
    )
    name = models.CharField(max_length=255, verbose_name="اسم المنتج")
    slug = models.SlugField(unique=True, verbose_name="الرابط")
    description = models.TextField(blank=True, verbose_name="الوصف")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="السعر"
    )
    is_active = models.BooleanField(default=True, verbose_name="متاح")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="المنتج"
    )
    image = models.ImageField(upload_to='products/', verbose_name="الصورة")
    is_main = models.BooleanField(default=False, verbose_name="صورة رئيسية")

    class Meta:
        verbose_name = "صورة منتج"
        verbose_name_plural = "صور المنتجات"

    def __str__(self):
        return f"صورة - {self.product.name}"


class Inventory(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='inventory',
        verbose_name="المنتج"
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name="الكمية المتوفرة"
    )

    class Meta:
        verbose_name = "المخزون"
        verbose_name_plural = "المخزون"

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
