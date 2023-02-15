from django.db import models


from account.models import User


class Resume(models.Model):
    CHOICES = (
        ('from media', 'from media'),
        ('from sanfransico', 'sarafannor radio'),
        ('my answer', 'other')
    )
    # name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume_name')
    # email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume_email')
    # phone = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume_phone')
    # city = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume_city')
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    git_hub = models.URLField()
    description = models.TextField()
    resume = models.FileField(upload_to='vacancy_resume/')
    about_us = models.TextField(choices=CHOICES)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'


