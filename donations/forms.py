
from django import forms
from .models import Order


class donationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
        }