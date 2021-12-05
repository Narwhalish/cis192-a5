from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, related_name="User", on_delete=models.CASCADE, null=True
    )
    body = models.CharField(max_length=280, blank=False)
    liked_by = models.ManyToManyField(User, through="Like")

    def __str__(self):
        return self.body[:14]

    def get_datetime(self):
        return self.created_at.strftime("%b %d %Y %H:%M:%S")

    def get_hashtags(self):
        return [k[1:] for k in self.body.split() if k.startswith("#")]

    def contains_hashtags(self):
        return self.get_hashtags() != []


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "tweet")
