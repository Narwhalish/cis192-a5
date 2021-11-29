from django.shortcuts import render
from core.models import Tweet

# Create your views here.
def login(request):
    return render(request, "core/login.html", {})


def home(request):
    return render(request, "core/home.html", {"tweets": Tweet.objects.all()})


def profile(request):
    return render(request, "core/profile.html", {})


def hashtag(request):
    return render(request, "core/hashtag.html", {})
