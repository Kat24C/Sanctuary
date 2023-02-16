from django import forms
from .models import AdoptionQuestion


class AdoptionDetails(forms.ModelForm):
    class Meta:
        model = AdoptionQuestion
        fields = '__all__'
