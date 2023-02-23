from django.db import models
from django.contrib.auth.models import User


TypesOfPets = (
    ("CAT", 'Cat'),
    ("DOG", 'Dog'),
    ("RABBIT", 'Rabbit'),
    ("GUINEA PIGS", 'Guinea pigs'),
    ("BIRDS", ' BIRDS'),
)

YesNo = (
    ("NO", 'No'),
    ("YES", 'Yes'),
)

Place = (
    ("INSIDE", 'Inside'),
    ("OUTSIDE", 'Outside'),
    ("ANIMAL HOUSE", 'Outdoor animal house')
)


class AdoptionQuestion(models.Model):
    """
    A user profile model for maintaining information.
    """
    perspective_pet_parent = models.CharField(max_length=40, null=True,
                                              blank=True)
    User_email = models.EmailField(max_length=70, blank=True, unique=True)
    other_pets = models.CharField(max_length=10,
                                  choices=YesNo,
                                  blank=True)
    please_give_details = models.TextField(max_length=400, blank=True)
    what_type_of_pet = models.CharField(max_length=11,
                                        choices=TypesOfPets,
                                        blank=True)
    pet_you_want = models.TextField(max_length=400)
    where_will_the_pet = models.CharField(max_length=20,
                                          choices=Place,
                                          blank=True)

    def __str__(self):
        return self.perspective_pet_parent
