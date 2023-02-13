from django.db import models

from account.models import User

class Resume(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='name')
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email')
    phone = models.ForeignKey(User, on_delete=models.CASCADE, related_name='phone')
    city = models.ForeignKey(User, on_delete=models.CASCADE, related_name='country')
    git_hub = models.URLField(blank=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.phone

    class Meta:
        verbeuse_name = 'Resume'
        plural_verbouse_name = 'Resumes'


