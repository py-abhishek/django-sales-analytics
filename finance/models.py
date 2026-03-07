from django.db import models
from django.utils.timezone import localdate

# Create your models here.

class ExpenseCategory(models.Model):
    name = models.CharField(db_index=True, max_length=100, unique=True)
    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, related_name="expenses", db_index=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    expense_date = models.DateField(db_index=True, default=localdate)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
