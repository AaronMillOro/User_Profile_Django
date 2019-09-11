from django.core.exceptions import ValidationError
import re


def password_validator(username, password):
    '''Setup special conditionals'''
    rgx_characters = re.compile(r'[A-Za-z]+')
    rgx_digits = re.compile(r'[0-9]+')
    rgx_special_characters = re.compile(r'[!@#$%^&*(),.?":{}|<>]+')

    if len(password) < 14:
        # Minimum password length of 14 characters.
        raise ValidationError('Password should have at least 13 characters')

    elif not rgx_characters.findall(''.join(sorted(password))):
        # Must use of both uppercase and lowercase letters
        raise ValidationError('Use both UPPER and LOWERcase letters')

    elif not rgx_digits.findall(''.join(sorted(password))):
        # Must contain 1 digit
        raise ValidationError('Password must contain at least 1 DIGIT')

    elif not rgx_special_characters.findall(''.join(sorted(password))):
        # Match any special characters
        raise ValidationError('Special characters required: @,$,%,etc.')
        
    elif username in password.lower():
        # password cannot contain username
        raise ValidationError('Password is too similar to username')
    else:
        return True
