from django import forms
from .models import AdoptionQuestions


class AdoptionDetails(forms.ModelForm):
    class Meta:
        model = AdoptionQuestions
        fields = '__all__'
