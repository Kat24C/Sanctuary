from django import forms
from .models import AboutTheAnimal


class PetDetails(forms.ModelForm):
    class Meta:
        model = AboutTheAnimal
        fields = '__all__'
