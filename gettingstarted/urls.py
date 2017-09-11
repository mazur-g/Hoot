from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
from django.contrib.staticfiles.urls import static
from django.conf import settings
# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^map/$', hello.views.map, name='map'),
    url(r'^profile/$', hello.views.profile, name='profile'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG is False:   #if DEBUG is True it will be served automatically
    urlpatterns += url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})