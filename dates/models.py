from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from phonenumber_field import phonenumber

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=CASCADE)
    # Confirm that first name, last name and e-mail are already been defined into User class

    nickname = models.CharField(max_length=30, help_text="How would you like to be called")
    phonenumber = PhoneNumberField()

class Remember(models.Model):

    date = models.DateField()
