from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request):
    n1=int(input("enter the 1st number:"))
    n2=int(input("enter the 2nd number:"))
    n3=n1+n2
    msg="sum="+str(n3)
    return HttpResponse(msg)