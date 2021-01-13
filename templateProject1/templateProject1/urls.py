
from django.contrib import admin
from django.urls import path
from templateApp1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('response/',views.my_view)
]
