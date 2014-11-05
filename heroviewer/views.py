from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from heroviewer.models import Hero

# Create your views here.
def index(request):
    """
    Simple overview over all heroes
    """
    allHeroes = Hero.objects.all()
    return render(request, 'heroviewer/index.html', {'heroList' :allHeroes})

def heroView(request, heroID):
    """
    Detail view of a hero
    """
    requestedHero = get_object_or_404(Hero, pk=heroID)
    return render(request, 'heroviewer/hero.html', {'hero': requestedHero})