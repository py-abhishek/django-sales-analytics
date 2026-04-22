from rest_framework import serializers

from purchases.models import Supplier, Purchase


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'phone', 'email', 'address']

class PurchaseSerializer(serializers.ModelSerializer):
    supplier = serializers.StringRelatedField()
    payment_method = serializers.CharField(source='get_payment_method_display')

    class Meta:
        model = Purchase
        fields = ['id', 'supplier', 'purchase_date', 'payment_method', 'total_amount']