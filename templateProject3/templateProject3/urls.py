
from django.contrib import admin
from django.urls import path
from templateApp3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('response/',views.dateTimeView)
]
