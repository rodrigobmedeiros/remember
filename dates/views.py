import calendar

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
        date__year=year,
        date__month=month)

    context = {"reminders": reminders}
    return render(
        request=request,
        template_name='dates/reminders.html',
        context=context)


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

@login_required
def delete_reminder(request, id):

    reminder = Reminder.objects.filter(id=id)
    reminder.delete()

    return redirect('main')
