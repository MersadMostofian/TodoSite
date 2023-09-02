from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import userRegisterForm,userLoginForm
from django.contrib import messages

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'],cd['email'],cd['password'])
            user.first_name = cd['firstname']
            user.last_name = cd['lastname']
            user.save()
            messages.success(request,'User Registered Successfully','success')
            return redirect('homePage')
    else:
        form = userRegisterForm()
    return render(request,'register.htm',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = userLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'User Loged in Successfully','success')
                return redirect('homePage')
            else:
                messages.error(request,'Username or Password is Wrong','danger')
            
    else:
        form = userLoginForm()
    return render(request,'login.htm',{'form':form})

def user_logout(request):
    logout(request)
    messages.success(request,'User Loged Out Successfully','success')
    return redirect('homePage')

def user_info(request):
    user = User.objects.get(username=request.user)
    return render(request,'info.htm',{'username':user.username,'firstname':user.first_name,'lastname':user.last_name,'email':user.email})