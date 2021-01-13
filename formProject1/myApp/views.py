from django.shortcuts import render
from myApp.forms import Student
def view1(request):
    f=Student()
    if request.method=="POST":
        f=Student(request.POST)
        if f.is_valid():
            name=f.cleaned_data['name']
            roll=f.cleaned_data['roll']
            marks=f.cleaned_data['marks']
            place=f.cleaned_data['place']
            d={'name1':name,'roll1':roll,'marks1':marks,'place1':place}
            return render(request,'myApp/output.html',d)
    d={'form':f}
    return render(request,'myApp/input.html',d)


