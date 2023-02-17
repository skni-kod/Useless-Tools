from django.shortcuts import render
import string
from random import choice
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'core/home.html')


def generator(request):
    return render(request, 'core/generator.html')


def password(request):
    if request.method == 'POST':
        length = int(request.POST.get('length'))
        uppercase = request.POST.get('uppercase')
        symbols = request.POST.get('symbols')
        numbers = request.POST.get('numbers')
        lowercase = request.POST.get('lowercase')
        chars = []
        if (lowercase):
            chars.extend(string.ascii_lowercase)
        if (uppercase):
            chars.extend(string.ascii_uppercase)
        if (symbols):
            chars.extend('!@#$%^&*')
        if (numbers):
            chars.extend('1234567890')
        generated_PASS = ''
        if (numbers or lowercase or symbols or uppercase):
            for x in range(length):
                generated_PASS += choice(chars)
        else:
            generated_PASS = 'zaznacz cos wrr'
        return JsonResponse({'password': generated_PASS})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()

        messages.success(request, 'Twoje konto zostało utworzone!')

        return redirect('signin')

    return render(request, 'core/signup.html')


def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            messages.success(request, 'Zalogowano pomyślnie!')
            return render(request, 'core/home.html', {'user': user})
        else:
            messages.error(request, 'Błędny login lub hasło!')
            return redirect('signin')

    return render(request, 'core/signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'Wylogowano pomyślnie!')
    return redirect('home')
