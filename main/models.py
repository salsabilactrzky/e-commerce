import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Product(models.Model):
    category_choices = [
        ('Clothes', 'Clothes'),
        ('Bag', 'Bag'),
        ('Shoes', 'Shoes'),
        ('Accessories', 'Accessories'),
        ('Other', 'Other'),
    ]
    condition_choices = [
        ('Fair', 'Fair'),
        ('Good', 'Good'),
        ('Like New', 'Like New')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50, choices=category_choices)
    brand = models.CharField(max_length=50, null=True, blank=True)
    condition = models.CharField(max_length=50, choices=condition_choices)
    stock = models.PositiveBigIntegerField()
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def is_sold(self):
        return self.stock <= 0
    
    def is_positive(self):
        if self.price <= 0:
            raise ValidationError('Price must be a positive number')
        if self.stock <= 0:
            raise ValidationError('Stock must be a positive number')