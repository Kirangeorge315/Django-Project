
from django.contrib import admin
from django.urls import path
from DBApp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('response/',views.view1)
]
