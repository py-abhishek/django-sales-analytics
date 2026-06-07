from django.db import models


class Customer(models.Model):
    """
    Represents a buyer
    """

    class Meta:
        ordering = ['-is_walkin','name']
        constraints = [
            models.UniqueConstraint(
                fields=['business', 'phone'],
                name='unique_phone_perbusiness'
            )
        ]

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200, blank=True)
    is_walkin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='customers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
