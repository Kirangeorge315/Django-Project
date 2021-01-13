from django.http import HttpResponse
def view1(request):
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    print(a/b) #trying to access a webpage but page is not available
    print("Inside View Function")
    return HttpResponse("<h1>successfully landed on webpage</h1>")