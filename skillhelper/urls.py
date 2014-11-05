# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from skillhelper import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
       # Index page /skillhelper/
       url(r'^$', views.indexView, name='index'),
       # /skillhelper/skill/skillName/
       url(r'^skill/(?P<skillID>[a-zA-Z]+)/$', views.skillDetailsView, name="skillDetails"),
       # /skillhelper/new/
       url(r'^new/$', views.newSkillView, name='newSkill'),
       # /skillhelper/new/add/
       url(r'^new/add/$', views.addSkill, name='addSkill'),
       )