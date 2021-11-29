from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, related_name="User", on_delete=models.CASCADE, null=True
    )
    body = models.TextField(max_length=280)

    def __str__(self):
        return self.body[:14]

    def get_datetime(self):
        return self.created_at.strftime("%b %d %Y %H:%M:%S")
