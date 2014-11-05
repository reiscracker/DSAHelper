from django.conf.urls import patterns, include, url
from django.contrib import admin
from heroviewer import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
       # Index page /heroviewer/
       url(r'^$', views.index, name='index'),
       # /heroviewer/hero/name/
       # url(r'^hero/(?P<heroID>[a-zA-Z]*)/$', views.heroView, name="hero"),
      url(r'^hero/(?P<heroID>\d+)/$', views.heroView, name="hero"),

       # # /poll/5/results/
       # url(r'^(?P<pk>\d+)/result/$', views.ResultView.as_view(), name='result'),
       # # /polls/5/vote/
       # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
       )