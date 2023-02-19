# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# class Payment(models.Model):
#    """
#    A user profile model for maintaining information.
#    """
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    first_name = models.CharField(max_length=40, null=True, blank=True)
#    surname = models.CharField(max_length=40, null=True, blank=True)
#    email = models.EmailField(max_length=70, blank=True, unique=True)
#    donation = models.BooleanField(default=False)

#    def __str__(self):
#        return self.user.username


# @receiver(post_save, sender=User)
# def create_user_payment(sender, instance, created, **kwargs):
#    if created:
#        Payment.objects.create(user=instance)
