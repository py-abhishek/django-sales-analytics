from django.db import models
from django.utils.timezone import localdate
from django.core.validators import MinValueValidator

# Create your models here.

class Supplier(models.Model):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='suppliers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):

    class PaymentMethod(models.TextChoices):

        CASH = 'cash', 'Cash'
        CARD = 'card', 'Card'
        UPI = 'upi', 'UPI'

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,
        null=True,
        db_index=True,
        related_name='purchases'
        )
    purchase_date = models.DateField(db_index=True, default=localdate)
    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(1)]
        )
    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,
        default=PaymentMethod.CASH
        )
    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='purchases')
    created_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_purchases')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PurchaseItem(models.Model):

    purchase = models.ForeignKey(
        Purchase,
        on_delete=models.CASCADE,
        related_name='items'
        )
    product = models.ForeignKey(
        'inventory.Product',
        on_delete=models.PROTECT,
        related_name='purchase_items'
        )
    quantity = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)]
        )
    unit = models.CharField(
        max_length=20,
        )
    unit_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
        )
    item_total_cost = models.DecimalField(
        # quantity * product purchase cost
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
        )
    
    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='purchase_items')


    def __str__(self):
        return self.product.name
    

