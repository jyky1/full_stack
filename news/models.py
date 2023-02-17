from django.db import models

from account.models import User


class News(models.Model):
    image = models.ImageField(upload_to='for_photo/')
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title, self.description
    


class Comment(models.Model):
    body = models.TextField()
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commets')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.body
    

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='likes')
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.news} liked by {self.author.name}'