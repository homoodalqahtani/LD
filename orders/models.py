from django.db import models
from core.models import User
from catalog.models import Product


class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name="المستخدم"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء"
    )

    class Meta:
        verbose_name = "سلة"
        verbose_name_plural = "سلال التسوق"

    def __str__(self):
        return f"سلة {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="السلة"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name="المنتج"
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="الكمية"
    )

    class Meta:
        verbose_name = "عنصر سلة"
        verbose_name_plural = "عناصر السلة"

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد المعالجة'),
        ('paid', 'مدفوع'),
        ('shipped', 'تم الشحن'),
        ('completed', 'مكتمل'),
        ('cancelled', 'ملغي'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name="العميل"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="حالة الطلب"
    )
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="إجمالي المبلغ"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الطلب"
    )

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب رقم {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="الطلب"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name="المنتج"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="سعر الوحدة"
    )
    quantity = models.PositiveIntegerField(
        verbose_name="الكمية"
    )

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return self.product.name


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('mada', 'مدى'),
        ('stc', 'STC Pay'),
        ('visa', 'Visa / Mastercard'),
    ]

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='payment',
        verbose_name="الطلب"
    )
    method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS,
        verbose_name="طريقة الدفع"
    )
    is_successful = models.BooleanField(
        default=False,
        verbose_name="تم الدفع"
    )
    transaction_id = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="رقم العملية"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الدفع"
    )

    class Meta:
        verbose_name = "عملية دفع"
        verbose_name_plural = "عمليات الدفع"

    def __str__(self):
        return f"دفع الطلب رقم {self.order.id}"
