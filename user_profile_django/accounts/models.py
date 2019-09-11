from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    #first_name = models.CharField(max_length=255, blank=True)
    #last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(null=True,blank=True,unique=True)
    date_birth = models.DateField(null=True,blank=True)
    avatar = models.ImageField(
        upload_to='images/', null=True, blank=True)
    bio = models.TextField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    fav_animal = models.CharField(max_length=255, blank=True)
    hobby = models.CharField(max_length=255, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
