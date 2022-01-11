import calendar
import datetime
from django.http.response import HttpResponse

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ReminderForm
from .models import Reminder

MONTH_NAMES_TO_NUMBERS = {
    v: k for k, v in enumerate(calendar.month_abbr[1:], start=1)
}


@login_required
def reminders(request):
    user = request.user
    month_name, year = request.GET["monthYear"].split(" ")
    month = MONTH_NAMES_TO_NUMBERS[month_name[:3]]

    reminders = Reminder.objects.filter(
        user=user,
        date__year__lte=year,
        date__month=month
    )

    context = {
        "reminders": reminders,
    }
    return render(
        request=request,
        template_name='dates/reminders.html',
        context=context)


@login_required
def main(request):

    user = request.user
    
    # Get current month and year
    today = datetime.datetime.now()

    reminders = Reminder.objects.filter(
        user=user,
        date__year__lte=today.year,
        date__month=today.month
    )

    context = {
        'reminders': reminders,
    }

    return render(
        request=request,
        template_name='dates/main.html',
        context=context)

@login_required
def delete_reminder(request, id):
    #TODO include user in the filter
    reminder = Reminder.objects.filter(
        user = request.user,
        id=id
    )

    reminder.delete()
    
    user = request.user
    month_name, year = request.GET["monthYear"].split(" ")
    month = MONTH_NAMES_TO_NUMBERS[month_name[:3]]

    reminders = Reminder.objects.filter(
        user=user,
        date__year__lte=year,
        date__month=month
    )

    context = {
        "reminders": reminders,
    }
    return render(
        request=request,
        template_name='dates/reminders.html',
        context=context)

@login_required
def add_reminder(request):

    user = request.user

    reminder_form = ReminderForm(request.POST)

    if reminder_form.is_valid():

        reminder_form = reminder_form.save(commit=False)
        reminder_form.user = user
        reminder_form.save()
        messages.success(request, ('Your reminder was successfully added!'))

    month_name, year = request.POST["monthYear"].split(" ")
    month = MONTH_NAMES_TO_NUMBERS[month_name[:3]]

    reminders = Reminder.objects.filter(
        user=user,
        date__year__lte=year,
        date__month=month
    )

    context = {
        "reminders": reminders,
    }
    return render(
        request=request,
        template_name='dates/reminders.html',
        context=context)

@login_required
def profile(request):

    return render(
        request=request,
        template_name='dates/profile.html'
    )