from django.db import models
from slugify import slugify



class Company(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=30, primary_key=True, blank=True, unique=True)
    description = models.TextField(max_length=250, blank=True)
    tagline = models.CharField(max_length=50, blank=True)
    logo = models.ImageField(blank=True)
    location = models.CharField(max_length=100, blank=True)



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save()

    def __str__(self) -> str:
        return self.name