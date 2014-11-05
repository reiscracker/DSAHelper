# -*- coding: utf-8 -*-
from django.contrib import admin
from heroviewer.models import Hero
from skillhelper.admin import AbilitiesInLine

# Register your models here.

class HeroAdmin(admin.ModelAdmin):
    # Define the list overview presentation
    list_display = ["name", "race", "sex", "culture", "profession", "age"]
    search_fields = ["name", "profession", "race"]

    # Define presentation of hero detail view
    fieldsets = (
        (None, {
            'fields': ["name"]
        }),
        ("Aussehen", {
            'fields': [ ["sex", "age", "weight", "hair_color", "eye_color"] ]
        }),
        ("Zugehörigkeit", {
            'fields': [ ["race", "culture", "profession", "social_status"] ]
        }),
        ("Basiswerte", {
            'fields': [ ["koerperkraft", "konstitution", "mut", "klugheit"],
                        ["intuition", "charisma", "fingerfertigkeit","gewandtheit"] ]
        })

    )
    inlines = [AbilitiesInLine]

admin.site.register(Hero, HeroAdmin)
