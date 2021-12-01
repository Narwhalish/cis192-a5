from django.http.response import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from core.models import Tweet

# Create your views here.
def login(request):
    if request.method == "POST":
        return redirect(reverse("home"))
    else:
        context = {"title": "Login"}

        return render(request, "core/login.html", context)


def home(request):
    if request.method == "POST":
        Tweet.objects.create(
            author=request.user,
            body=request.POST["body"],
        )

        return redirect(reverse("home"))
    else:
        context = {"title": "Home", "tweets": Tweet.objects.all()[::-1]}

        return render(request, "core/home.html", context)


def profile(request):
    context = {"title": "Profile"}

    return render(request, "core/profile.html", context)


def hashtag(request):
    context = {"title": "Hashtags"}

    return render(request, "core/hashtag.html", context)
