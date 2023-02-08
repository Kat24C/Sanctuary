from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class HomePage(models.Model):
    """
    A home page recipe for the mission statement, and decription
    block on how people can help. Include title, statement and date.
    """
    name = models.CharField(max_length=100, unique=True, blank=False)
    description = models.CharField(max_length=500)
    date = models.DateField(auto_created=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
