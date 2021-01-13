from django.shortcuts import render
from DBApp1.models import Student
# Create your views here.
def view1(request):
    e=Student.objects.all()
    d={'emp':e}
    return render(request,'DBApp1/1.html',d)
