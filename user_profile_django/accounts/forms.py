from django import forms
from django.contrib.auth.models import User

from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = (
            'date_birth',
            'bio',
            'avatar',
            'city',
            'state',
            'country',
            'residence',
            'fav_animal',
            'hobby',
            )
