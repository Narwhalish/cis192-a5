from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, related_name="User", on_delete=models.CASCADE, null=True
    )
    body = models.CharField(max_length=280, blank=False)
    # HashContains = [k for k in body.split() if k.startswith("#")]

    def __str__(self):
        return self.body[:14]

    def get_datetime(self):
        return self.created_at.strftime("%b %d %Y %H:%M:%S")

    def get_Hash_Array(self):
        return self.HashContains

    def contains_Hash(self, hashtag):
        return hashtag in self.HashContains

    def HasHashtags(self):
        return self.HashContains != []
