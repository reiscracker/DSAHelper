# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Hero(models.Model):
    SEX_MALE = "m"
    SEX_FEMALE = "f"
    SEX_CHOICES = ( (SEX_MALE, "Männlich"), (SEX_FEMALE, "Weiblich") )

    name = models.CharField("Name", max_length=50)
    race = models.CharField("Rasse", max_length=30)
    culture = models.CharField("Kultur", max_length=30)
    profession = models.CharField("Profession", max_length=30)
    sex = models.CharField("Geschlecht", choices=SEX_CHOICES, max_length=1, default=SEX_FEMALE)
    age = models.PositiveSmallIntegerField("Alter")
    weight = models.PositiveSmallIntegerField("Gewicht")
    hair_color = models.CharField("Haarfarbe", max_length=20)
    eye_color = models.CharField("Augenfarbe", max_length=20)
    social_status = models.PositiveSmallIntegerField("Sozialstatus")

    koerperkraft = models.PositiveSmallIntegerField()
    konstitution = models.PositiveSmallIntegerField()
    mut = models.PositiveSmallIntegerField()
    klugheit = models.PositiveSmallIntegerField()
    intuition = models.PositiveSmallIntegerField()
    charisma = models.PositiveSmallIntegerField()
    fingerfertigkeit = models.PositiveSmallIntegerField()
    gewandtheit = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    def getBaseskillsAsList(self):
        baseSkills = [
            self.koerperkraft, self.konstitution, self.mut, self.klugheit,
            self.intuition, self.charisma, self.fingerfertigkeit, self.gewandtheit
        ]
        return baseSkills

