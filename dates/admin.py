from django.contrib import admin

# Register your models here.


from dates.models import Reminder, Profile
# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Reminder)
admin.site.register(Profile)