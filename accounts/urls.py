from django.conf.urls import include, url

from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout,{'template_name': 'registration/logout.html'}, name='logout'),
	url(r'^register/$',views.register_page, name='register'),

]