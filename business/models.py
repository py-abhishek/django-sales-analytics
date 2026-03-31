from django.db import models

# Create your models here.

class Business(models.Model):

    class BusinessTypeChoices(models.TextChoices):
        RETAIL = 'retail', 'Retail'
        WHOLESALE = 'wholesale', 'Wholesale'
        SERVICE = 'service', 'Service'
        OTHER = 'other', 'Other'


    name = models.CharField(max_length=200)
    business_type = models.CharField(max_length=20, choices=BusinessTypeChoices.choices, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    created_by = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='businesses')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


# Link between user and business
class Membership(models.Model):

    class UserRoleChoices(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        STAFF = 'staff', 'Staff'


    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='memberships')
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=UserRoleChoices.choices)

    is_active =  models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'business'],
                name='unique_user_business'
            )
        ]
        indexes = [
            models.Index(fields=['user', 'business'])
        ]

    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.business.name}'



