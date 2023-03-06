from django.shortcuts import reverse, render
import string
from random import choice
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from django.views.generic import CreateView



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


class Signup(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse('signin')
    
