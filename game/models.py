from django.db import models
from slugify import slugify

from company.models import Company


class Game(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, primary_key=True, blank=True, unique=True)
    poster = models.ImageField(upload_to='poster/', blank=True)
    compony = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='game' )
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save()

    def __str__(self) -> str:
        return self.name


    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Game'
        verbose_name_plural = 'Games'


class Rating(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self) -> str:
        return f'{self.rating} -> {self.game.name}'

    def avg_rating(self):
        from django.db.models import Avg
        result = self.ratings.aggregate(Avg('rating'))
        return result['rating__avg']