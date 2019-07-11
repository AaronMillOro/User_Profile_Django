from django import forms
from django.core import validators

from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            "first_name",
            "last_name",
            "email",
            "date_birth",
            "bio",
            "avatar",
            ]
