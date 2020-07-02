from django.shortcuts import render
from django.http import HttpResponse
import random, string

def home(request):
    return render(request, 'generator/home.html', {'title':'Home'})

def password(request):
    lcase = string.ascii_lowercase
    ucase = string.ascii_uppercase
    nums = string.digits
    spec = string.punctuation
    combo = []
    thepassword = ''

    for i in lcase:
        combo.append(i)

    if request.GET.get('uppercase')=='y':
        for i in ucase:
            combo.append(i)

    if request.GET.get('numbers')=='y':
        for i in nums:
            combo.append(i)

    if request.GET.get('special')=='y':
        for i in spec:
            combo.append(i)

    length = int(request.GET.get('length', 12))

    for i in range(length):
        thepassword += random.choice(combo)

    return render(request, 'generator/password.html', {'password' : thepassword})

def about(request):
    return render(request, 'generator/about.html')
