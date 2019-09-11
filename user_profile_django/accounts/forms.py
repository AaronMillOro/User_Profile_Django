from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
import re

from . import models


class UserForm(forms.ModelForm):
    '''Populates auth.model User fields'''
    first_name = forms.CharField(label=('First name'))
    last_name  = forms.CharField(label=('Last name'))

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    '''Extended fields that will fill accounts_profile table'''
    confirm_email = forms.EmailField(label='Verify email')
    date_birth = forms.DateField(
        input_formats=['%m/%d/%Y', '%m/%d/%y', '%Y-%m-%d',],
        label='Date of birth (ex. MM/DD/YYYY, MM/DD/YY, YYYY-MM-DD)')

    class Meta:
        model = models.Profile
        fields = (
            'email', 'confirm_email', 'date_birth',
            'bio', 'avatar', 'city', 'state', 'country', 'fav_animal','hobby',
        )
        labels = {
            'bio': 'Short biography', 'fav_animal': 'Favorite animal',
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


class ChangePasswordForm(PasswordChangeForm):
    '''Change user password by using adapted validators'''

    def clean(self, *args, **kwargs):
        ''' set variables for validators'''
        user = self.user
        old_pw = self.cleaned_data.get('old_password')
        new_pw1 = self.cleaned_data.get('new_password1')
        first_name = user.first_name.lower()
        last_name = user.last_name.lower()
        username = user.username.lower()
        rgx_characters = re.compile(r'[A-Za-z]+')
        rgx_digits = re.compile(r'[0-9]+')
        rgx_special_characters = re.compile(r'[!@#$%^&*(),.?":{}|<>]+')

        if old_pw == new_pw1:
            # Password must not be the same as the current password
            raise ValidationError('NEW and OLD passwords cannot be the same')

        elif len(new_pw1) < 14:
            # Minimum password length of 14 characters.
            raise ValidationError('''A strong password should have
            more than 13 characters''')

        elif not rgx_characters.findall(''.join(sorted(new_pw1))):
            # Must use of both uppercase and lowercase letters
            raise ValidationError('''Password must use both UPPER and
            LOWERcase letters''')

        elif not rgx_digits.findall(''.join(sorted(new_pw1))):
            # Must contain 1 digit
            raise ValidationError('Password must contain at least 1 DIGIT')

        elif not rgx_special_characters.findall(''.join(sorted(new_pw1))):
            # Match any special characters
            raise ValidationError('''Password must have special characters!
            Such as: @, #, $, %, etc.''')

        elif first_name in new_pw1.lower():
            # password cannot contain first_name
            raise ValidationError('''Cannot contain first name''')

        elif last_name in new_pw1.lower():
            # password cannot contain last_name
            raise ValidationError('''Cannot contain last name''')

        elif username in new_pw1.lower():
            # password cannot contain username
            raise ValidationError('''Password is too similar to username''')
