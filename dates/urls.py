from django.contrib import admin
from django.urls import path

from dates import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('profile/', views.profile, name='profile'), 
    path('reminders/', views.reminders, name='reminders'),
    path('add-reminder', views.add_reminder, name='add-reminder'),
    path('delete-reminder/<int:id>', views.delete_reminder, name='delete-reminder')
]
