# -*- coding: utf-8 -*-
from django.db import models
from heroviewer.models import Hero

# Create your models here.

class Talent(models.Model):
    name = models.CharField(max_length=50)
    KK = 1
    KO = 2
    MU = 3
    KL = 4
    IN = 5
    CH = 6
    FF = 7
    GE = 8
    BASETALENTS_CHOICES = (
        (KK, 'Körperkraft'),
        (KO, 'Konstitution'),
        (MU, 'Mut'),
        (KL, 'Klugheit'),
        (IN, 'Intuition'),
        (CH, 'Charisma'),
        (FF, 'Fingerfertigkeit'),
        (GE, 'Gewandtheit'),
    )
    requiredTalent1 = models.PositiveSmallIntegerField("Benötigtes Talent",
                               choices=BASETALENTS_CHOICES, default=KK)
    requiredTalent2 = models.PositiveSmallIntegerField("Benötigtes Talent",
                               choices=BASETALENTS_CHOICES, default=KK)
    requiredTalent3 = models.PositiveSmallIntegerField("Benötigtes Talent",
                               choices=BASETALENTS_CHOICES, default=KK)
    def __str__(self):
        return self.name

class Ability(models.Model):
    hero = models.ForeignKey(Hero)
    talent = models.ForeignKey(Talent)
    improvement = models.SmallIntegerField("Verbesserung")
    def __str__(self):
        return "Ability of hero " + self.hero.name + " for skill " + self.talent.name
