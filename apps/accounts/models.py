from django.db import models
from django.contrib.auth.models import AbstractUser 

# we are going to create a User model here

class User(AbstractUser):

    GENDER_CHOICES  = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

