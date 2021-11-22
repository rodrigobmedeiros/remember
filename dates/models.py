from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class MessageType(models.TextChoices):

    WHATSAPP = 'Whatsapp'

class EventTypeOptions(models.TextChoices):

    BIRTHDAY = 'Birthday'
    WEDDING_ANNIVERSARY = 'Wedding Anniversary'
    RELATIONSHIP_ANNIVERSARY = 'Relationship Anniversary'
    BILL_PAYMENT = 'Bill Payment'
    OTHER = 'Other'

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30, help_text="How would you like to be called")

class Contact(models.Model):

    phone_number = PhoneNumberField()
    message_type = CharField(max_length=30, choices=MessageType.choices, default=MessageType.WHATSAPP)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class EventType(models.Model):

    event_type = models.CharField(max_length=30, choices=EventTypeOptions.choices, default=EventTypeOptions.BIRTHDAY)

    # I'm thinking about the inclusion of user as foreign key... is it really needed?
    # Maybe to show all EventType used until certain time...
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Reminder(models.Model):

    date = models.DateField()
    description = models.CharField(max_length=200)
    related_person_name = models.CharField(max_length=100)
    monthly_reminder = models.BooleanField(default=False)
    yearly_reminder = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True)

class Event(models.Model):

    sending_datetime = models.DateTimeField(auto_now_add=True)
    successfully_sent = models.BooleanField(default=False)
    reminder_event = models.ForeignKey(Reminder, on_delete=models.SET_NULL, null=True)