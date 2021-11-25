from django.db import models

# Create your models here.
class Tweet(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
