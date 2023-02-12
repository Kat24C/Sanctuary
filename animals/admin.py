from django.contrib import admin
from .models import AboutTheAnimal


@admin.register(AboutTheAnimal)
class AnimalInfo(admin.ModelAdmin):
    """
    Admin access to models.py to update mission statement
    and how you can help.
    """
    list_display = ('animals_name',
                    'animal_nickname',
                    'featured_image',
                    'type_of_animal',
                    'approximate_age',
                    'about_the_animal')
