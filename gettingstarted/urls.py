from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'', include('log.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html'},
    url(r'^map/$', hello.views.map, name='map'),
    url(r'^admin/', include(admin.site.urls)),
]
