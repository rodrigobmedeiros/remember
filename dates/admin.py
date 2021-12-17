from django.contrib import admin

# Register your models here.


from dates.models import Reminder, Profile
# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Profile)

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ("date", "description", "related_person_name",
                    "monthly_reminder", "yearly_reminder",
                    "user", "event_type")
    search_fields = ("description", "user__username",
                     "event_type")


