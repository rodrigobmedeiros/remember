from django.shortcuts import render

# Create your views here.

def include_reminder(request):

    return render(
        request,
        template_name="hello_world.html"
    )