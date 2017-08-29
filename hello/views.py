from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    return render(request, 'index.html')

def map(request):
    return render(request, 'map.html')

def map_x(request):
    if request.method == 'POST':
        if 'x' in request.POST:
            x = request.POST['x']
            # doSomething with pieFact here...
            return HttpResponse('success') # if everything is OK
    # nothing went well
    return HttpRepsonse('FAIL!!!!!')

def map_y(request):
    if request.method == 'POST':
        if 'y' in request.POST:
            y = request.POST['y']
            # doSomething with pieFact here...
            return HttpResponse('success') # if everything is OK
    # nothing went well
    return HttpRepsonse('FAIL!!!!!')

def signin(request):
    return render(request, 'login.html')


