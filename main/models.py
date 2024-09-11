from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, null=True, blank=True)
    condition = models.CharField(max_length=50)
    stock = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def is_sold(self):
        return self.stock <= 0