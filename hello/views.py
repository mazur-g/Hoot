"""
This module implements the view functions - functions that are excecuting while user connects to url defined in urls.py module
"""



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
from random import random
from django.core.management import call_command
from accounts.models import UserProfile

# Create your views here.
def index(request):
    """

    Function is responsible for actions while opening home page.
    In fact it just evokes the template 'index.html'

    Args:
    request (:obj:`HttpRequest`): the request object used to generate this response.
    Returns:
    (:obj:`HttpResponse`): the HttpResponse object.

    """
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
                geo_lon = form.cleaned_data['longitude']
                geo_lat = form.cleaned_data['latitude']
                if geo_message.lower() == 'korosu'.lower():
                    form.veryspecial = 2
                else:
                    form.veryspecial = 1
                g = GeoIP()
                ip = get_client_ip(request)
                if ip:
                    location = g.coords(ip)
                if geo_lon != -10000 and geo_lat != -10000:
                    location = [geo_lon, geo_lat]
                file_path = os.path.join(settings.STATIC_ROOT, 'kmldata.kml')
                datas = open(file_path,"r")
                data_tmp = datas.read()[:-27]
                datas.close()
                open('file_path','w').close()
                with open(file_path,'r+') as datas:
                    datas.write(data_tmp+'\n\n<Placemark id="'+request.user.username+', '+strftime("%Y-%m-%d %H:%M:%S", gmtime())+
                    '">\n\t<name>'+strftime("%Y-%m-%d %H:%M:%S", gmtime())+': '
                    +request.user.username+' posts: '+str(geo_message)+
                    '</name>\n'
                    '\t<magnitude>1.0</magnitude>\n'
                    '\t<Point>\n'
                    '\t\t<coordinates>'+str(float(location[0])+random()/10000)+','+str(float(location[1])+random()/10000)+
                    ',0</coordinates>\n'
                    '\t</Point>\n'
                    '</Placemark>'
                    '\n</Folder></Document></kml>')
                call_command('collectstatic', verbosity=0, interactive=False)
                userProfile = UserProfile.objects.get(user=request.user)
                userProfile.hoots+=1
                userProfile.save()
        else:
            form = GeoMessageForm()
        return render(request, 'map.html', {'form': form})
    else:
        return redirect("{% url 'accounts:login' %}", permanent=False)

@login_required
def profile(request):
    """

    Function is responsible for actions while opening "Your profile" from home page.
    It allows to make changes in your own profile, validates implemented values.

    Args:
    request (:obj:`HttpRequest`): the request object used to generate this response.
    Returns:
    (:obj:`HttpResponse`): the HttpResponse object with profile changes if everything is good or HttpResponse object
    with error messages otherwise.
    
    """
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


