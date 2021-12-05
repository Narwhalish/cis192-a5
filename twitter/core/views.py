from django.shortcuts import render, redirect
from django.urls import reverse
from core.models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth import (
    login as _login,
    authenticate as _authenticate,
    logout as _logout,
)


def login(request):
    if request.method == "POST":
        user = _authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )

        if user:
            _login(request, user)
            return redirect(reverse("home"))

    context = {"title": "Login"}

    return render(request, "core/login.html", context)


def signup(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST["username"],
            email=request.POST["email"],
            password=request.POST["password"],
        )

        _login(request, user)
        return redirect(reverse("home"))

    context = {"title": "Login"}

    return redirect(reverse("login"), context)


def logout(request):
    _logout(request)

    return redirect(reverse("login"))


def home(request, filter="all"):
    if request.method == "POST":
        Tweet.objects.create(
            author=request.user,
            body=request.POST["body"],
        )

        return redirect(reverse("home"))

    if request.user.is_authenticated:
        tweets = Tweet.objects.all().order_by("-created_at")
        context = {
            "title": "Home",
            "tweets": tweets
            if (filter == "all")
            else tweets.filter(author=request.user),
        }

        return render(request, "core/home.html", context)

    return redirect(reverse("login"))


def profile(request):
    context = {"title": "Profile"}

    return render(request, "core/profile.html", context)


def hashtag(request):
    context = {"title": "Hashtags"}

    return render(request, "core/hashtag.html", context)
