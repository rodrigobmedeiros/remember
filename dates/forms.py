from .models import Reminder, Profile, User
from django.forms import ModelForm, widgets

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

        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'})
        }

class UserForm(ModelForm):

    class Meta:
        model = User 

class ProfileForm(ModelForm):
    pass