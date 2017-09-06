from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import UserProfile
from accounts.forms import ChangeUserProfileForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from hello.forms import GeoMessageForm
from django.contrib.gis.geoip import GeoIP
import os
from django.conf import settings
from time import gmtime, strftime
from random import randint


# Create your views here.
def index(request):
    return render(request, 'index.html')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@login_required
def map(request):
    if request.user.is_active:
        if request.method == "POST":
            form = GeoMessageForm(data=request.POST)
            if form.is_valid():
                geo_message = form.cleaned_data['message']
                g = GeoIP()
                ip = get_client_ip(request)
                if ip:
                    location = g.coords(ip)
                file_path = os.path.join(settings.STATIC_ROOT, 'rgdata.xht')
                with open(file_path,"a") as datas:
                    datas.write('\n\n<Placemark id="'+request.user.username+', '+strftime("%Y-%m-%d %H:%M:%S", gmtime())+
                    '">\n\t<name>'+request.user.username+', '+strftime("%Y-%m-%d %H:%M:%S", gmtime())+': '+str(geo_message)+
                    '</name>\n'
                    '\t<magnitude>1.0</magnitude>\n'
                    '\t<Point>\n'
                    '\t\t<coordinates>'+str(location[0])+','+str(location[1])+',0</coordinates>\n'
                    '\t</Point>\n'
                    '</Placemark>')
        else:
            form = GeoMessageForm()
        return render(request, 'map.html', {'form': form})
    else:
        return redirect("{% url 'accounts:login' %}", permanent=False)

@login_required
def profile(request):
    if request.user.is_active:
        userProfile = UserProfile.objects.get(user=request.user)
        form = ChangeUserProfileForm()
        if request.method == "POST":
            form = ChangeUserProfileForm(request.POST,request.FILES)
            if form.is_valid():
                user = request.user
                userProfile = UserProfile.objects.get(user=user)
                userProfile.image = request.FILES.get('new_image',userProfile.image)
                if request.POST.get('new_email'):
                    user.email = request.POST.get('new_email')
                user.save()
                userProfile.save()
                context = {'userProfile' : userProfile, 'form' : form}
                return render(request,'profile.html',context)
        variables = RequestContext(request,{'form' : form, 'userProfile' : userProfile})
        return render_to_response('profile.html',variables)
    else:
        return redirect("{% url 'accounts:login'}", permanent=False)


