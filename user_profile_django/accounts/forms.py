from django import forms
from django.contrib.auth.models import User

from . import models


class ProfileForm(forms.ModelForm):
    '''Extended fields that will full accounts_profile table '''
    confirm_email = forms.EmailField(label='Verify email')
    date_birth = forms.DateField(
        input_formats=['%m/%d/%Y', '%m/%d/%y', '%Y-%m-%d',],
        label='Date of birth (ex. MM/DD/YYYY, MM/DD/YY, YYYY-MM-DD)')

    class Meta:
        model = models.Profile
        fields = (
            'first_name',
            'last_name',
            'email',
            'confirm_email',
            'date_birth',
            'bio',
            'avatar',
            'city',
            'state',
            'country',
            'fav_animal',
            'hobby',
            )
        labels = {
            'bio': 'Short biography',

            'fav_animal': 'Favorite animal',
            }

    def clean_bio(self):
        ''' Validation that biography has 10 or more characters'''
        bio = self.cleaned_data['bio']
        if len(bio) < 10:
            raise forms.ValidationError(
                'The biography must have at least 10 characters')
        return bio

    def clean_confirm_email(self):
        ''' Validation of email address '''
        email = self.cleaned_data.get('email')
        confirm_email = self.cleaned_data.get('confirm_email')
        if email == confirm_email:
            return confirm_email
        else:
            raise forms.ValidationError('Verify email please')
