import calendar
import datetime
from django.http.response import HttpResponse

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ReminderForm, UserForm, ProfileForm, ContactForm
from .models import Contact, Profile, Reminder

MONTH_NAMES_TO_NUMBERS = {
    v: k for k, v in enumerate(calendar.month_abbr[1:], start=1)
}


@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def profile(request):

    user = request.user
    profile = Profile.objects.filter(user=user).first()

    if request.POST:

        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile = profile_form.save(commit=False)
            profile_form.instance.user = user
            profile_form.save()

    else:

        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(
        request=request,
        template_name='dates/profile.html',
        context=context
    )

@login_required(login_url='/accounts/login/')
def contact(request):

    user = request.user
    contact = Contact.objects.filter(user=user).first()

    if request.POST:

        contact_form = ContactForm(request.POST, instance=contact)

        if contact_form.is_valid():

            contact_form.instance.user = user
            contact_form.save()

    else:
        
        contact_form = ContactForm(instance=contact)
    
    context = {
        'contact_form': contact_form
    }

    return render(
        request=request,
        template_name='dates/contact.html',
        context=context
    )
