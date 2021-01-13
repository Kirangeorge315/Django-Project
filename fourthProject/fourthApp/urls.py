from django.contrib import admin
from django.urls import path
from fourthApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('response1/',views.view1),
    path('response2/',views.view2),
    path('response3/',views.view3)
]