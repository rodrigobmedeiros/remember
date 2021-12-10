from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ReminderForm
from .models import Reminder

# Create your views here.

@login_required
def add_reminder(request):

    if request.method == 'POST':

        reminder_form = ReminderForm(request.POST) 

        if reminder_form.is_valid():

            reminder_form = reminder_form.save(commit=False)
            reminder_form.user = request.user
            reminder_form.save()
            messages.success(request, ('Your reminder was successfully added!'))

    user = request.user
    reminders = Reminder.objects.filter(user=user)

    context = {
        'reminders': reminders
    }

    return render(
        request=request,
        template_name='dates/main.html',
        context=dict(**{'reminder_form': reminder_form}, **context)
    )

@login_required
def main(request):
    if request.method == 'POST':

        reminder_form = ReminderForm(request.POST) 

        if reminder_form.is_valid():

            reminder_form = reminder_form.save(commit=False)
            reminder_form.user = request.user
            reminder_form.save()
            messages.success(request, ('Your reminder was successfully added!'))

    user = request.user
    reminders = Reminder.objects.filter(user=user)

    context = {
        'reminders': reminders
    }

    return render(
        request=request,
        template_name='dates/main.html',
        context=context)