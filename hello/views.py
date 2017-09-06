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
                #return HttpResponse("Twoja lokacja ciulu: "+str(location[0])+', '+str(location[1])+'\nTwoja wiadomość ciulu: '+str(geo_message))
                with open("/hello/static/rgdata.xht","a") as datas:
                    datas.seek(0, os.SEEK_END)
                    while datas.tell() and datas.read(1) != '\n':
                        datas.seek(-2, os.SEEK_CUR)
                    datas.truncate()
                    datas.write('<entry> <title>'+request.user.username+'\'s post</title> '
                                '<published>DATA</published>'
                                '<content type="html">'+str(geo_message)+'L</content>]'
                                ' <author> <name>'+ request.user.username +'</name> </author> <georss:point>'+location[0]+' '
                                +location[1]+'</georss:point> <geo:lat>'+location[0]+'</geo:lat> <geo:long>'
                                +location[1]+'</geo:long> <woe:woeid>03955</woe:woeid> </entry> \n\n</feed>')
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


