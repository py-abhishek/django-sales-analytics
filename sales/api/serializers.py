from rest_framework import serializers

from sales.models import Customer, Sale


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'email', 'address']

class SaleSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    payment_method = serializers.CharField(source='get_payment_method_display')

    class Meta:
        model = Sale
        fields = ['id', 'customer', 'customer', 'sale_date', 'payment_method', 'total_amount', 'total_profit']