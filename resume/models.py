from django.db import models


from account.models import User


class Resume(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume')
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume')
    phone = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume')
    city = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume')
    git_hub = models.URLField(blank=True)
    description = models.TextField()
    resume = models.FileField(blank=True)
    about_us = models.TextChoices()

    def __str__(self) -> str:
        return self.resume.name

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'


