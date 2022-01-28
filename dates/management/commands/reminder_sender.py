from django.core.management import BaseCommand
from django.conf import settings
from django.db.models import Q
from dates.models import Reminder, Contact
from twilio.rest import Client
import datetime


class Command(BaseCommand):

    help = 'Send all reminders for an specific day'

    def handle(self, *args, **options):

        print("Test if it's running...")

        # TODO: 
        # 1 - get current day

        today = datetime.datetime.now()

        # 2 - get all reminders that must be send for that day
        #   2.1 - analyze day if reminder is monthly
        #   2.2 - verify day and month if reminder is yearly

        monthly_condition = Q(monthly_reminder=True, date__day=today.day)
        yearly_condition = Q(yearly_reminder=True, date__day=today.day, date__month=today.month)

        reminders = Reminder.objects.filter(monthly_condition | yearly_condition)

        # 3 - Connect with twilio
        twilio_client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        
        users_contacts = dict()

        # For each reminder
        for reminder in reminders:
            
            # 4 - get user
            user = reminder.user

            # 5 - get contact for this user
            contact = users_contacts.setdefault(user, Contact.objects.filter(user=user).first().phone_number)
            
            # 6 - create a message based on user and reminder
            message = f'related_name: {reminder.related_person_name}\n'
            message += f"Don't forget the {reminder.event_type}\n"
            message += f'Date: {reminder.date}'

            # 7 - send message       
            twilio_message = twilio_client.messages.create(
                body=message,
                from_=f'whatsapp:{settings.TWILIO_NUMBER}',
                to=f'whatsapp:{contact}'

            )

            # TODO:
            # Persist all send events into event table