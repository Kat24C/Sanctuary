from django.db import models
from cloudinary.models import CloudinaryField


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = CloudinaryField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
