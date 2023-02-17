from django.contrib import admin

from .models import Vacancy, Team, Role

admin.site.register(Team)
admin.site.register(Role)
admin.site.register(Vacancy)