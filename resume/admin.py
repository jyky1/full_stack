from django.contrib import admin

from .models import Resume


# class ResumeInline(admin.TabularInline):

    # model = Resume
admin.site.register(Resume)
