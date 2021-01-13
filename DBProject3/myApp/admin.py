from django.contrib import admin
from myApp.models import Customer
class CustomerAdmin(admin.ModelAdmin):
    l=['name','age','mail','ph']
admin.site.register(Customer,CustomerAdmin)    

# Register your models here.
