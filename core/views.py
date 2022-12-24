from django.shortcuts import render
from random import choice

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
        chars = list('qwertyuiopasdfghjklzxcvbnm')
        if(uppercase):
            chars.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
        if(symbols):
            chars.extend('!@#$%^&*')
        if(numbers):
            chars.extend('123456789')
        generated_PASS = ''
        for x in range(length):
            generated_PASS += choice(chars)
        return render(request,'core/generator.html',{'password':generated_PASS})
