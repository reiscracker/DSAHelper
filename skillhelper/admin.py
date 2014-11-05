# -*- coding: utf-8 -*-
from django.contrib import admin
from skillhelper.models import Hero, Talent, Ability

# Register your models here.
class AbilitiesInLine(admin.TabularInline):
    model = Ability
    extra = 0


class TalentAdmin(admin.ModelAdmin):
    list_display = ["name", "requiredTalent1", "requiredTalent2", "requiredTalent3"]
    search_fields = ["requiredTalent1", "requiredTalent2", "requiredTalent3", "name"]

    fieldsets = [
        (None, {
            'fields' : ["name"]
        }),
        ("Benötigte Talente", {
            'fields' : ["requiredTalent1", "requiredTalent2", "requiredTalent3"]
        })
    ]
admin.site.register(Talent, TalentAdmin)