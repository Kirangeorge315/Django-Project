from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from myApp.forms import signupForm
# Create your views here
def home_view(request):
    return render(request,'myApp/home.html')
@login_required
def java_view(request):
    return render(request,'myApp/javaexams.html')
@login_required
def python_view(request):
    return render(request,'myApp/pythonexams.html')
@login_required
def aptitude_view(request):
    return render(request,'myApp/aptitudeexams.html')
def logout_view(request):
    return render(request,'myApp/logout.html')    
def signupView(request):
    f=signupForm()
    if request.method=='POST':
        f=signupForm(request.POST)
        user=f.save()
        user.set_password(user.password) #takes care of hashing
        user.save()
        return redirect("accounts/login")
    d={"form":f}
    return render(request,'myApp/signup.html',d)   