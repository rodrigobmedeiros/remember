from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class MessageType(models.TextChoices):

    WHATSAPP = 'Whatsapp'

class EventType(models.TextChoices):

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

class Reminder(models.Model):

    date = models.DateField()
    description = models.CharField(max_length=200)
    related_person_name = models.CharField(max_length=100)
    monthly_reminder = models.BooleanField(default=False)
    yearly_reminder = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class EventType(models.Model):

    # I keep only this table removing the field from reminder model
    # Here although we have choices, it's not exactly a constrain so the user can include a custom text
    # I'm not shure if it's a good practice =D
    event_type = models.CharField(max_length=30, choices=EventType.choices, default=EventType.BIRTHDAY)

    # I'm not shure if I want to delete the event type because I can use that information maybe to improve options in the future.
    reminder_event = models.ForeignKey(Reminder, on_delete=models.DO_NOTHING)

class Event(models.Model):

    # it's kind of a log of sent messages, so i want to keep all entries.
    # In this case would be better put a deleted boolean field on reminder model and
    # instead of delete a reminder, only mark as deleted.
    sending_datetime = models.DateTimeField(auto_now_add=True)
    successfully_sent = models.BooleanField(default=False)
    reminder_event = models.ForeignKey(Reminder, on_delete=models.DO_NOTHING)