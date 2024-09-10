from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50, null=True, blank=True)
    condition = models.CharField(max_length=50, null=True, blank=True)
    stock = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    sold = models.BooleanField(default=False)


    def __str__(self):
        return self.name


    @property
    def is_sold(self):
        return self.sold and self.stock <= 0