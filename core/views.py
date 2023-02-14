from django.shortcuts import render
import string
from random import choice
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def home(request):
  return render(request,'core/home.html')


def generator(request):
    return render(request,'core/generator.html')

def password(request):
    if request.method == 'POST':
        length = int(request.POST.get('length'))
        uppercase = request.POST.get('uppercase')
        symbols = request.POST.get('symbols')
        numbers = request.POST.get('numbers')
        lowercase = request.POST.get('lowercase')
        chars = []
        if(lowercase):
            chars.extend(string.ascii_lowercase)
        if(uppercase):
            chars.extend(string.ascii_uppercase)
        if(symbols):
            chars.extend('!@#$%^&*')
        if(numbers):
            chars.extend('1234567890')
        generated_PASS = ''
        if(numbers or lowercase or symbols or uppercase):
            for x in range(length):
                generated_PASS += choice(chars)
        else:
            generated_PASS = 'zaznacz cos wrr'
        return JsonResponse({'password': generated_PASS})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        myuser = User.objects.create_user(username,email,password)
        myuser.save()

        messages.success(request,'Twoje konto zostało utworzone!')

        return redirect('signin')
       
    return render(request,'core/signup.html')

def signin(request):
    return render(request,'core/signin.html')

def signout(request):
    pass


