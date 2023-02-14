from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=30, unique=True, primary_key=True)
    poster = models.ImageField(upload_to='poster/', blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'


# class Rating(models.Model):
#     rating = models.PositiveSmallIntegerField()
    