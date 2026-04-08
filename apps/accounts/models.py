from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser 

# we are going to create a User model here

class User(AbstractUser):

    class GenderChoice(models.TextChoices):
        M = 'Male',
        F = 'Female'

    
    phone = models.CharField(max_length=15, unique=True, blank=True, default="")
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    bio = models.TextField(blank=True, default="")
    gender=models.CharField(
            max_length=10, 
            choices=GenderChoice.choices, 
            blank=True,
        )
    birth_date = models.DateField(null=True, blank=True)

