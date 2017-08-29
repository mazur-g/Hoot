from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    return render(request, 'index.html')

def map(request):
    if request.method == 'POST':
            x = request.POST['x']
            y = request.POST['y']
            # doSomething with pieFact here...
            return render(request, 'map.html') # if everything is OK
    # nothing went well
    return HttpRepsonse('FAIL!!!!!')


def signin(request):
    return render(request, 'login.html')


