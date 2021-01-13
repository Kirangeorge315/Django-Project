from django.shortcuts import render
from myApp.models import Student
# Create your views here.
def view1(request):
    s=Student.objects.all()
    d={'stud':s}
    return render(request,'myApp/1.html',d)



# Create your views here.
