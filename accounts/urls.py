from django.conf.urls import include, url

from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout,{'template_name': 'registration/logout.html'}, name='logout'),
	url(r'^register/$',views.register_page, name='register'),
	url(r'^register/redirect/$', views.redirect_page, name='redirect'),
	url(r'^search/$',views.search_user, name='search'),
	url(r'^(?P<username>\w+)/$', views.profile_page, name='profile'),

]