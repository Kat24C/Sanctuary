from django import forms
from .models import HomePage


class MissionForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = (
            'name',
            'description',
            'date',
        )
