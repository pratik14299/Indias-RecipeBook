from django.http import HttpResponse
from django.shortcuts import render,redirect
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def userRegister(request):
    form = UserCreationForm()
    print(request.method) 
    template_name = 'auth/reg.html'
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_url")
        else:
            return HttpResponse("Not Valid")
    context = {
        'form':form
    }

    return render(request,template_name,context)

def loginUser(request):
    template_name = "auth/login.html"
    if request.method == "POST":
        un = request.POST.get("un")
        pwd = request.POST.get("pwd")
        user = authenticate(username = un,password = pwd)
        print(f'{user}')
        if user is not None:
            login(request,user)
            return redirect("home_url")
        else:
            messages.add_message(request, messages.INFO, 'please check username or password')
    context = {}
    return render(request,template_name,context) 

def logoutUser(request):
    logout(request)
    return redirect("login_url")