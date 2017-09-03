from django.shortcuts import render, get_object_or_404,redirect
from .forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from  django.core.urlresolvers import reverse
# Create your views here.


def login(request):
	return render(request,'register/login.html')

def logout(request):
	logout(request)
	return render(request,'register/logout.html')


def register_page(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST,request.FILES)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
			image = request.FILES.get('image','img/default2.jpg')
			userProfile = UserProfile.objects.create(user=user,image=image)
			return redirect('index')
	form = RegistrationForm()
	variables = RequestContext(request,{'form':form})
	return render_to_response('registration/register.html',variables)


@login_required
def search_user(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			try: 
				name = request.POST['name']
				get_object_or_404(User,username=name)
				return redirect(reverse('accounts:profile',args=[name]))
			except:
				redirect('accounts:search')
	form = SearchForm()
	variables = RequestContext(request,{'form' : form })
	return render_to_response('search_user.html',variables)



	return render(request,'search_user.html')

@login_required
def profile_page(request,username):
	user = get_object_or_404(User, username=username)
	userProfile = UserProfile.objects.get(user=user)
	context = {'userProfile' : userProfile}
	return render(request,'profile_page.html',context)
