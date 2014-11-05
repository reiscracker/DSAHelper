# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from skillhelper.models import Talent, Ability
from heroviewer.models import Hero

# Create your views here.
def indexView(request):
    heroes = Hero.objects.all()
    if not heroes:
        return render(request, 'skillhelper/noheroes.html')
    return render(request, 'skillhelper/index.html', {'heroes': heroes})

def skillDetailsView(request, skillID):
    return HttpResponse("Skill detail view")

def newSkillView(request):
    return HttpResponse("New skill view")

def addSkill(request):
    return HttpResponse("Adding new skill to database")