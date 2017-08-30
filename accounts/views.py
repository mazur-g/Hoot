from django.shortcuts import render
from .forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
# Create your views here.


def login(request):
	return render(request,'register/login.html')

def logout(request):
	logout(request)
	return render(request,'register/logout.html')


def register_page(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
			return HttpResponseRedirect('/')
	form = RegistrationForm()
	variables = RequestContext(request,{'form':form})
	return render_to_response('registration/register.html',variables)