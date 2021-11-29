from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, related_name="User", on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=140)
    body = models.TextField()

    def __str__(self):
        return self.title
