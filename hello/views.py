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
from .models import Greeting

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def map(request):
    if request.user.is_active:
        if request.method == "POST":
                x = request.POST['x']
                y = request.POST['y']
                with open("/hello/static/rgdata.xht","a") as datas:
                    datas.write('<entry> <title>NOWY_POST</title> <published>DATA</published><content type="html">ZAWARTOSC HTML</content> <author> <name>AUTOR</name> </author> <georss:point>'+str(x)+' '+str(y)+'</georss:point> <geo:lat>'+str(x)+'</geo:lat> <geo:long>'+str(y)+'</geo:long> <woe:woeid>142344433</woe:woeid> </entry>')
                return HttpResponse(str(x)+' '+str(y)+' It works pirlitirli!') # if everything is OK
        # nothing went well
        return render(request, 'map.html')
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


