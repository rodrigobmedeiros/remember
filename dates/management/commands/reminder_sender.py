from django.core.management import BaseCommand
from django.conf import settings
from django.db.models import Q
from dates.models import Reminder

import datetime


class Command(BaseCommand):

    help = 'Send all reminders for an specific day'

    def handle(self, *args, **options):

        print("Test if it's running...")

        # TODO: 
        # 1 - get current day

        today = datetime.datetime.now()
        print(f'{today.day}/{today.month}/{today.year}')

        # 2 - get all reminders that must be send for that day
        #   2.1 - analyze day if reminder is monthly
        #   2.2 - verify day and month if reminder is yearly

        monthly_condition = Q(monthly_reminder=True, date__day=today.day)
        yearly_condition = Q(yearly_reminder=True, date__day=today.day, date__month=today.month)

        reminders = Reminder.objects.filter(monthly_condition | yearly_condition)

        print(reminders)

        # 3 - Connect with twilio
        twilio_account_sid = settings.TWILIO_ACCOUNT_SID
        twilio_auth_token = settings.TWILIO_AUTH_TOKEN

        print(twilio_account_sid)
        print(twilio_auth_token)

        # For each reminder
        # 4 - get user
        # 5 - get contact for this user
        # 6 - create a twilio client with this info
        # 7 - create a message based on user and reminder
        # 8 - send messages