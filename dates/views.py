from django.shortcuts import render
from django.contrib import messages
from .forms import ReminderForm
from .models import Reminder

# Create your views here.

def add_reminder(request):

    if request.method == 'POST':

        reminder_form = ReminderForm(request.POST)

        if reminder_form.is_valid():
            reminder_form.save()
            messages.success(request, ('Your reminder was successfully added!'))

        else:
            messages.error(request, ('Error saving form'))

    reminder_form = ReminderForm()

    return render(
        request=request,
        template_name='dates/add_reminder.html',
        context={'reminder_form': reminder_form}
    )