from django.db import models
from django.core.validators import MinValueValidator
from django.utils.timezone import localdate
# Create your models here.


class Customer(models.Model):
    """
    Represents a buyer
    """

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Sale(models.Model):
    """
    Represents one sales transaction with a customer
    Includes all products sold to that customer
    """

    class PaymentMethod(models.TextChoices):
        """
        Contains different payment options
        """

        CASH = "cash", "Cash"
        CARD = "card", "Card"
        UPI = "upi", "UPI"

    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        db_index=True,
        related_name="sales"
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SaleItem(models.Model):
    """
    This is a bridge between sale and product.
    This will handle all products bought by a customer
    """

    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        related_name="items"
        )
    product = models.ForeignKey(
        "inventory.Product",
        on_delete=models.PROTECT,
        related_name="sale_items"
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
    item_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
        )
    item_profit = models.DecimalField(max_digits=12, decimal_places=2, default=0)


    def __str__(self):
        return self.product.name
    
