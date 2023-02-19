from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class UserDonation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    donation_amount = models.DecimalField(max_digits=10,
                                         decimal_places=2,
                                         null=False,
                                         default=0)
    payment_bool = models.BooleanField(default=False)
    stripe_pd = models.CharField(max_length=250)


@receiver(post_save, sender=User)
def create_user_donation(sender, instance, created, **kwargs):
    if created:
        UserDonation.objects.create(user=instance)
