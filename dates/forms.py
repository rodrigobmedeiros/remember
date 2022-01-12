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
        fields = (
            'first_name',
            'last_name',
            'username',
            'email'
        )

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'readonly': True})
        self.fields['email'].widget.attrs.update({'readonly': True})