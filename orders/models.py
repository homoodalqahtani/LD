from django.db import models
from core.models import User
from catalog.models import Product


class Cart(models.Model):
    """
    سلة المستخدم
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    """
    عناصر السلة
    """
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


class Order(models.Model):
    """
    الطلب النهائي
    """
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
        related_name='orders'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    """
    عناصر الطلب
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name}"


class Payment(models.Model):
    """
    الدفع
    """
    PAYMENT_METHODS = [
        ('mada', 'مدى'),
        ('stc', 'STC Pay'),
        ('visa', 'Visa / Mastercard'),
    ]

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='payment'
    )
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    is_successful = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order #{self.order.id}"
