from django.shortcuts import render
from django.contrib import messages
from .forms import ReminderForm
from django.contrib.auth.decorators import login_required


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

    reminder_form = ReminderForm()

    return render(
        request=request,
        template_name='dates/add_reminder.html',
        context={'reminder_form': reminder_form}
    )