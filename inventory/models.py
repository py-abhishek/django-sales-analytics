from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class ProductCategory(models.Model):
    """
    To Organize products into groups
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Represents an item being sold
    """

    class UnitChoices(models.TextChoices):
        PIECE = "pcs", "Pieces"
        KILOGRAM = "kg", "Kilograms"
        LITER = "l", "Liters"
        GRAM = "g", "Grams"
        METER = "m", "Meters"
        BOX = "box", "Boxes"
        PACK = "pack", "Packs"

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    sku = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.PROTECT,
        db_index=True,
        related_name="products"
        )
    cost_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
        )
    selling_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
        )
    stock_quantity = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
        )
    unit = models.CharField(
        max_length=20,
        choices=UnitChoices.choices
        )
    reorder_level = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
        )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

