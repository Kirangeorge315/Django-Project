from django.shortcuts import render

# Create your views here.
def view1(request):
    myName="Shreenath"
    favPlayer="MS.Dhoni"
    favAnimal="Lion"
    favSubject="Python"
    d={'name':myName,'player':favPlayer,'animal':favAnimal,'subject':favSubject}
    return render(request,'staticApp1/1.html',d)