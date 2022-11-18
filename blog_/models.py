from django.db import models
from django.contrib.auth.models import User
import PIL

# Create your models here.
class Post(models.Model):
    """Post wstawiony przez admina"""
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(default="")
    content = models.TextField(default="")
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/', blank=True, unique=True)

    def __str__(self):
        """Zwraca reprezentację modelu w postaci ciągu tekstowego."""
        return f'"{self.title[:50]}" {self.description[:50]}...'

class Comment(models.Model):
    """Komentarze wstawiane przez użytkowników"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Zwraca reprezentację modelu w postaci ciągu tekstowego."""
        return f'{self.text[:50]}...'

class Like(models.Model):
    """Dodawanie likeow"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Zwraca reprezentację modelu w postaci ciągu tekstowego."""
        return f'{self.post.title} | {self.owner} | {self.date_added}'