from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=250)
    datetime = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
