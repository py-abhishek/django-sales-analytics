from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Category(models.Model):
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
        KILOGRAM = "kg", "Kilogram"
        LITER = "l", "Liter"
        GRAM = "g", "Gram"
        METER = "m", "Meter"
        BOX = "box", "Box"
        PACK = "pack", "Pack"

    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT,
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
        choices=UnitChoices.choices,
        default=UnitChoices.PIECE
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

