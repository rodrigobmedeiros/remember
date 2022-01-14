from .models import Reminder, Profile, User, Contact
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
        )

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = (
            'nickname',
        )

class ContactForm(ModelForm):

    class Meta:

        model = Contact 
        fields = (
            'phone_number',
            'messagem_type'
        )