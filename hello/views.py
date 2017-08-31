from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    return render(request, 'index.html')

def map(request):
    if user.is_active:
        if request.method == 'POST':
                x = request.POST['x']
                y = request.POST['y']
                with open("/hello/static/rgdata.xht","a") as datas:
                    datas.write('<entry> <title>NOWY_POST</title> <published>DATA</published><content type="html">ZAWARTOSC HTML</content> <author> <name>AUTOR</name> </author> <georss:point>'+str(x)+' '+str(y)+'</georss:point> <geo:lat>'+str(x)+'</geo:lat> <geo:long>'+str(y)+'</geo:long> <woe:woeid>142344433</woe:woeid> </entry>')
                return HttpResponse(str(x)+' '+str(y)+' It works pirlitirli!') # if everything is OK
        # nothing went well
        return render(request, 'map.html')
    else:
        return render(request, 'accounts:login')


