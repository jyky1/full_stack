from django.db import models


from account.models import User


class Resume(models.Model):
    CHOICES = (
        ('from media', 'from media'),
        ('from sanfransico', 'sarafannor radio'),
        ('other', 'my answer'),
    )
    # name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume_name')
    # email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume_email')
    # phone = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume_phone')
    # city = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume_city')
    CHOICES_CITY = (
        ('US', 'United States'),
        ('RU', 'Russia'),
        ('KG', 'Kyrgyzstan'),
        ('KZ', 'Kazakhastan'),
    )
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    last_name = models.CharField(max_length=30)
    git_hub = models.URLField()
    description = models.TextField()
    phone = models.CharField(max_length=10)
    country = models.CharField(max_length=30, choices=CHOICES_CITY)
    resume = models.FileField(upload_to='vacancy_resume/')
    about_us = models.CharField(max_length=20, choices=CHOICES)
    my_answer_for_about_us = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'


