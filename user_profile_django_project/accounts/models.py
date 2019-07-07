from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_birth = models.DateField()
    bio = models.TextField()
    avatar = models.ImageField(upload_to='images/')
