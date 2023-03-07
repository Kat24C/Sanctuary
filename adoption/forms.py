from django import forms
from .models import AdoptionQuestion
from phonenumber_field.formfields import PhoneNumberField


class AdoptionDetails(forms.ModelForm):
    class Meta:
        model = AdoptionQuestion
        fields = '__all__'

