from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('remember-admin-panel/', admin.site.urls),
    path('', include('dates.urls')),
    path('accounts/', include('allauth.urls'))
]
