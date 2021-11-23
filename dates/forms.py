from .models import Reminder
from django.forms import ModelForm

class ReminderForm(ModelForm):

    class Meta:
        model = Reminder
        fields = (
            'related_person_name',
            'date',
            'event_type',
            'description',
            'monthly_reminder',
            'yearly_reminder',
        )