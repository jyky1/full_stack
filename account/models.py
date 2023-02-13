from django.db import models


class User(models.Model):

    CHOICES = (
        ('US', 'United States'),
        ('RU', 'Russia'),
        ('KG', 'Kyrgyzstan'),
        ('KZ', 'Kazakhastan'),
    )

    username = models.CharField(max_length=60, blank=True)
    email = models.EmailField()
    phone = models.CharField(blank=True)
    country = models.CharField(max_length=300, choices = CHOICES)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=55, blank=True)