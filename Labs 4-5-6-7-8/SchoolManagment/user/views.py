from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required   
from user.decorators import isadmin ,isloggedin
from emails.views import send_welcome_email

# Create your views here.
@isloggedin
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user= form.save()
            username =user.username
            email = form.cleaned_data.get('email')
            messages.success(request, f'تم إنشاء الحساب بنجاح للمستخدم {username}! يمكنك الآن تسجيل الدخول.')
            send_welcome_email(username,email)
            return redirect('user:login')
        else:
            context = {'form': form}
            messages.error(request, 'Invalid username or password. Please try again.')
            return render(request, 'register.html', context)
    else:
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    
@isloggedin
def userlogin(request):
 
    
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            
            login(request,user)
            messages.success(request, f'أهلاً بعودتك، {user.username}!')
            return redirect('students:home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    
def userlogout(request):
    logout(request)
    return redirect('user:login')

# @login_required(login_url='user:login')
def home(request):
    return render(request, 'students/home.html')
