from django.shortcuts import render
from core.models import Tweet

# Create your views here.
def login(request):
    return render(request, "core/login.html", {"title": "Login"})


def home(request):
    context = {"title": "Home", "tweets": Tweet.objects.all()}

    return render(request, "core/home.html", context)


def profile(request):
    return render(request, "core/profile.html", {"title": "Profile"})


def hashtag(request):
    return render(request, "core/hashtag.html", {"title": "Hashtags"})
