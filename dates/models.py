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

# Contact table let user have more different contacts for different kind of messages.
# Starting only with whatsapp option, but in the future we can support other platforms.
class Contact(models.Model):

    phone_number = PhoneNumberField()
    message_type = CharField(max_length=30, choices=MessageType.choices, default=MessageType.WHATSAPP)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Reminder(models.Model):

    date = models.DateField()
    descritpion = models.CharField(max_length=200)

    # Include some default option to define the event type.
    event_type = models.CharField(max_length=30, choices=EventType.choices, default=EventType.BIRTHDAY)
    related_person_name = models.CharField(max_length=100)

    # Considering that yearly reminders are a specific case of monthly reminders, I only include a boolean to define if a will be send monthly or not.
    monthly_reminder = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserDefinedEventType(models.Model):

    # In case user choose "Other" option for event type, it's possible to include a message that will be stored into this table
    # is it make sense? =D
    event_type = models.CharField(max_length=30, help_text="Enter the Event Type")
    reminder_event = models.ForeignKey(Reminder, on_delete=models.CASCADE)

class EventStatus(models.Model):

    # Thinking about that
    # TODO
    pass
