from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

TypesOfAnimals = (
    ("CAT", 'Cat'),
    ("DOG", 'Dog'),
    ("RABBIT", 'Rabbit'),
    ("GUINEA PIGS", 'Guinea pigs'),
    ("BIRDS", ' Birds'),
)


class AboutTheAnimal(models.Model):
    """
    A model to describe the animals. This will include the name,
    type, age, about and species.
    """
    animals_name = models.CharField(max_length=200, null=True)
    animal_nickname = models.CharField(max_length=100, null=True, blank=False)
    featured_image = CloudinaryField('image', default='placeholder')
    type_of_animal = models.CharField(max_length=11,
                                      choices=TypesOfAnimals,
                                      default=1,
                                      blank=False)
    approximate_age = models.PositiveIntegerField(default=1)
    about_the_animal = models.TextField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.animals_name

    def animal_id(self):
        return reverse("pet_outline", kwargs={"pk": self.pk})
