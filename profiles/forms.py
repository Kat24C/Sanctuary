from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """

        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First name',
            'surname': 'Surname',
            'phone_number': 'Phone number',
            'street_address1': 'Street Address',
            'street_address2': 'Street Address',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Postcode',
            'country': 'country',
        }

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
