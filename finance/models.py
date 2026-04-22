from django.db import models
from django.utils.timezone import localdate
from django.core.exceptions import ValidationError

# Create your models here.

class ExpenseCategory(models.Model):
    name = models.CharField(db_index=True, max_length=100, unique=True)
    description = models.TextField(blank=True)
    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='expense_categories')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    expense_date = models.DateField(db_index=True, default=localdate)
    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='expenses')
    created_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_expenses')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
      # Override save
    def save(self, *args, **kwargs):
        if self.category:
            # Check for business inconsistancy
            if self.category.business != self.business:
                raise ValidationError('Expense and Category belong to different businesses')
            
        super().save(*args, **kwargs)
