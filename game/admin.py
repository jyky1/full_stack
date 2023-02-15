from django.contrib import admin

from .models import Game, Rating


class GameInline(admin.TabularInline):
    
    model = Game


class GameAdmin(admin.ModelAdmin):
    list_filter = ['rating__avg']
    search_fields = ['slug']
    list_display = ['name', 'rating_avg', 'description']
    inlines = [GameInline]