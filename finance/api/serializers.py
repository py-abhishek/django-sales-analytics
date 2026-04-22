from rest_framework import serializers

from finance.models import ExpenseCategory, Expense


class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Expense
        fields = ['id', 'name', 'expense_date', 'category', 'amount']

class ExpenseCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseCategory
        fields = ['id', 'name', 'description', 'created_at']