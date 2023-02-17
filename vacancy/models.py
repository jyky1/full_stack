from django.db import models
from slugify import slugify

from game.models import Game


class Team(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='team')
    titel = models.CharField(max_length=12)
    slug = models.SlugField(max_length=30, primary_key=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titel)
        super().save()

    def __str__(self) -> str:
            return f'{self.titel} k {self.game.name}'


    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class Role(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='role')
    titel = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, primary_key=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titel)
        super().save()

    def __str__(self) -> str:
        return self.titel 


    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


class Vacancy(models.Model):
    CHOICES_CITY = (
        ('US', 'United States'),
        ('RU', 'Russia'),
        ('KG', 'Kyrgyzstan'),
        ('KZ', 'Kazakhastan'),
    )
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='vacancy')
    group = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='vacancy')
    team = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='vacancy')
    location = models.CharField(max_length=30, choices=CHOICES_CITY)
    demands = models.TextField()
    privileges = models.TextField()


    def __str__(self) -> str:
        return self.team.name