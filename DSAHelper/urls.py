from django.conf.urls import patterns, include, url
from django.contrib import admin, staticfiles

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DSAHelper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Point to hero urls for /hero/
    url(r'^heroviewer/', include('heroviewer.urls', namespace='heroviewer')),
    url(r'^skillhelper/', include('skillhelper.urls', namespace='skillhelper')),

    url(r'^admin/', include(admin.site.urls)),
)