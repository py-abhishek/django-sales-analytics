from django.db import models
from django.core.validators import MinValueValidator
from django.utils.timezone import localdate
from django.core.exceptions import ValidationError

from sales.models import Customer
# Create your models here.


class Sale(models.Model):
    """
    Represents one sales transaction with a customer
    Includes all products sold to that customer
    """

    class PaymentMethod(models.TextChoices):

        CASH = 'cash', 'Cash'
        CARD = 'card', 'Card'
        UPI = 'upi', 'UPI'

    class StatusChoices(models.TextChoices):
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'

    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        db_index=True,
        related_name='sales'
        )
    sale_date = models.DateField(db_index=True, default=localdate)
    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(1)]
        )
    total_profit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,
        default=PaymentMethod.CASH
        )
    
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.COMPLETED, db_index=True)
    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='sales')
    created_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_sales')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def is_cancelled(self):
        return self.status == self.StatusChoices.CANCELLED
    
    # Override save
    def save(self, *args, **kwargs):
        if self.customer:
            # Validate business consitency 
            if self.customer.business != self.business:
                raise('Sale and Customer belongs to different businesses')
            
        super().save(*args, **kwargs)


class SaleItem(models.Model):
    """
    This is a bridge between sale and product.
    This will handle all products bought by a customer
    """

    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        related_name='items'
        )
    product = models.ForeignKey(
        'inventory.Product',
        on_delete=models.PROTECT,
        related_name='sale_items'
        )
    quantity = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)]
        )
    unit = models.CharField(
        max_length=20,
        )
    price_at_sale = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
        )
    cost_at_sale = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0
        )
    item_total_price = models.DecimalField(
        # quantity * product selling price
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
        )
    item_profit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='sale_items')


    def __str__(self):
        return self.product.name
    
    # Override save
    def save(self, *args, **kwargs):
        if self.sale and self.product:
            # Validate business consitency 
            if self.sale.business != self.product.business:
                raise ValidationError('Sale and Product belong to different businesses')
            
            self.business = self.sale.business # Enforce correct business
        super().save(*args, **kwargs)
    
