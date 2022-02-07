from django.core.management import BaseCommand
from django.conf import settings
from django.db.models import Q
from dates.models import Reminder, Contact, Event
from twilio.rest import Client
import datetime


class Command(BaseCommand):

    help = 'Send all reminders for an specific day'

    def handle(self, *args, **options):

        today = datetime.datetime.now()

        monthly_condition = Q(monthly_reminder=True, date__day=today.day)
        yearly_condition = Q(yearly_reminder=True, date__day=today.day, date__month=today.month)

        reminders = Reminder.objects.filter(monthly_condition | yearly_condition)

        # Create a twilio client is needed to be able to send messages
        twilio_client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        
        contacts = Contact.objects.all().select_related('user')

        user_contacts = {contact.user:contact.phone_number for contact in contacts}

        # Loop through all reminders for specific day.
        # Get reminder's user
        # Get contact's user
        # Create a new message
        # Send the reminder
        # Persist the reminder sending event on Event table
        for reminder in reminders:
            
            user = reminder.user

            contact = user_contacts.get(user)
            
            message = (
                f"*REMINDER:*\n"
                f"\n"
                f"Related Name: *{reminder.related_person_name}*\n"
                f"Don't forget the *{reminder.event_type}*\n"
                f"Date: *{reminder.date}*"
            )
            
            event = Event()
            event.reminder_event = reminder 

            twilio_message = twilio_client.messages.create(
                    body=message,
                    from_=f'whatsapp:{settings.TWILIO_NUMBER}',
                    to=f'whatsapp:{contact}'
                )

            event.successfully_sent = True  
            event.save()