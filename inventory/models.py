from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

# Create your models here.

class ProductCategory(models.Model):
    '''
    To Organize products into groups
    '''

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'business'],
                name='unique_procategory_perbusiness'
            )
        ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='product_categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    '''
    Represents an item being sold
    '''

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['sku', 'business'],
                name='unique_productsku_perbusiness'
            )
        ]

    class UnitChoices(models.TextChoices):
        PIECE = 'pcs', 'Piece'
        KILOGRAM = 'kg', 'KG'
        LITER = 'l', 'Liter'
        GRAM = 'g', 'Gram'
        METER = 'm', 'Meter'
        BOX = 'box', 'Box'
        PACK = 'pack', 'Pack'


    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    sku = models.CharField(max_length=100)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.PROTECT,
        db_index=True,
        related_name='products'
        )
    current_avg_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True
        )
    selling_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
        )
    current_stock = models.IntegerField(
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
    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='products')
    created_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    # Override save
    def save(self, *args, **kwargs):
        if self.category:
            # Check for business inconsistancy
            if self.category.business != self.business:
                raise ValidationError('Expense and Category belong to different businesses')
            
        super().save(*args, **kwargs)


# Record every stock movement (as history)
class InventoryLedger(models.Model):
    class TransTypeChoices(models.TextChoices):
        PURCHASE = 'pur', 'Purchase'
        SALE = 'sale', 'Sale'
        NEW_PRODUCT = 'new_product', 'New Product Added'
        ADJUSTMENT = 'adj', 'Adjustment'
        RETURN_IN = 'return_in', 'Return In'
        RETURN_OUT = 'return_out', 'Return Out'
        DAMAGE = 'dmg', 'Damage'
        CANCEL_SALE = 'cancel_sale', 'Cancel Sale'

    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    transaction_type = models.CharField(choices=TransTypeChoices.choices, db_index=True, max_length=20)
    quantity_change = models.IntegerField()
    before_quantity = models.IntegerField()
    after_quantity = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=12, decimal_places=2) # unit cost at that moment
    total_cost = models.DecimalField(max_digits=12, decimal_places=2)

    # Reference Linking with FKs (where Only ONE of these must be set per row)
    purchase = models.ForeignKey('purchases.Purchase', on_delete=models.PROTECT, null=True, blank=True)
    sale = models.ForeignKey('sales.Sale', on_delete=models.PROTECT, null=True, blank=True)
    # adjustment = models.ForeignKey('', on_delete=models.PROTECT, null=True, blank=True)
    
    
    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='stock_movements')
    created_at = models.DateTimeField(auto_now_add=True)

    # Override save
    def save(self, *args, **kwargs):
        if self.product_id:
            # Check for business inconsistancy
            if self.product.business != self.business:
                raise ValidationError('Invetory Ledger: Product Business missmatch')
            
            if self.purchase:
                if self.purchase.business != self.business:
                    raise ValidationError('Invetory Ledger: Purchase Business missmatch')
            elif self.sale:
                if self.sale.business != self.business:
                    raise ValidationError('Invetory Ledger: Sale Business missmatch')
                
        super().save(*args, **kwargs)
    
