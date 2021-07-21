from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.


def loginView(request):
    print(request.method, "Hello")
    if request.method=="POST":
        if request.POST is None:
            return HttpResponse('Please enter username & password')
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse('Invalid User')
    else:
        form = AuthenticationForm()
        return render(request,'registration/login.html', {'form' : form})

def logoutView(request):
    logout(request)
    return redirect('index')

def registerView(request):
    print('registration')
    if request.method=='POST':
        if request.POST is None:
            return HttpResponse('Enter valid details')
        else:
            form = UserCreationForm(request.POST)
            if(form.is_valid()):
                username = request.POST['username']
                password1 = request.POST['password1']
                password2 = request.POST['password2']
                user = User.objects.create_user(username=username,email=None, password=password1)
                user.save()
                userlog = authenticate(request,username=username, password=password1)
                login(request,userlog)
                return redirect('index')
            else:
                return HttpResponse('Enter correct credentials')
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form' : form})