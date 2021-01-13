from django.shortcuts import render
from myApp.models import Customer
def view1(request):
    e=Customer.objects.all()
    d={'Cust':e}
    return render (request,'myApp/1.html',d)

# Create your views here.
