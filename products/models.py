from django.db import models
from cloudinary.models import CloudinaryField


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField(null=True, blank=True)

    def __str__(self):
        return self.name
