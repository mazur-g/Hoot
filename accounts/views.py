from django.shortcuts import render, get_object_or_404,redirect
from .forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from  django.core.urlresolvers import reverse
# Create your views here.



def register_page(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST,request.FILES)
		if form.is_valid():
			user = User.objects.create_user(username=request.POST['username'],password = request.POST['password1'],email=request.POST['email'])
			image = request.FILES.get('image','img/default2.jpg')
			userProfile = UserProfile.objects.create(user=user,image=image)
			usr = authenticate(username=request.POST['username'],password=request.POST['password1'])
			if usr is not None:
				if usr.is_active:
					login(request,usr)
					print("login")
			else:
				print("not login")
			return redirect('accounts:register')
	variables = RequestContext(request,{'form':form})
	return render_to_response('registration/register.html',variables)

@login_required
def	redirect_page(request):
		return render(request,'redirect.html')




@login_required
def search_user(request):
	if request.method == 'POST':
		form = SearchForm(data=request.POST)
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
