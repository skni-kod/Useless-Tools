from django.shortcuts import render
import string
from random import choice
from django.http import JsonResponse


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
        chars = list(string.ascii_lowercase)
        if(uppercase):
            chars.extend(string.ascii_uppercase)
        if(symbols):
            chars.extend('!@#$%^&*')
        if(numbers):
            chars.extend('123456789')
        generated_PASS = ''
        for x in range(length):
            generated_PASS += choice(chars)
        return JsonResponse({'password': generated_PASS})



