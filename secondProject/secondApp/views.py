from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def my_view1(request):
    s="<h1>"+"this is 1st response"+"</h1>"
    return HttpResponse(s)
def my_view2(request):
    s="<h1>"+"this is 2nd response"+"</h1>"
    return HttpResponse(s)
def my_view3(request):
    s="<h1>"+"this is 3rd response"+"</h1>"
    return HttpResponse(s)
