from rest_framework import serializers

from inventory.models import Product, InventoryLedger, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    unit = serializers.CharField(source='get_unit_display')
    class Meta:
        model = Product
        fields = ['id', 'name', 'sku', 'current_avg_cost', 'selling_price', 'current_stock', 'unit', 'created_at']

class InventoryLedgerSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    unit = serializers.CharField(source='product.get_unit_display')
    transaction_type = serializers.CharField(source='get_transaction_type_display')

    class Meta:
        model = InventoryLedger
        fields = ['id', 'product', 'created_at', 'transaction_type', 'quantity_change', 'unit', 'before_quantity', 'after_quantity']



class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'description', 'created_at']