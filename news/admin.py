from django.contrib import admin

from .models import News, Like, Comment

admin.site.register(Like)
admin.site.register(News)
admin.site.register(Comment)