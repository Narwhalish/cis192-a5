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
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )

        if user:
            _login(request, user)
            return redirect(reverse("home"))

    context = {"title": "Login"}

    return render(request, "core/login.html", context)


def signup(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST.get("username"),
            email=request.POST.get("email"),
            password=request.POST.get("password"),
        )

        _login(request, user)
        return redirect(reverse("home"))

    context = {"title": "Login"}

    return redirect(reverse("login"), context)


def logout(request):
    _logout(request)

    return redirect(reverse("login"))


def home(request):
    if request.method == "POST":
        if request.POST.get("like"):
            tweet = Tweet.objects.get(id=request.POST.get("like"))

            if request.user in tweet.liked_by.all():
                tweet.liked_by.remove(request.user)
            else:
                tweet.liked_by.add(request.user)

            tweet.save()
        else:
            tweet = Tweet.objects.create(
                author=request.user,
                body=request.POST.get("body"),
            )
            tweet.liked_by.add(request.user)
            tweet.save()

        return redirect(request.get_full_path())

    if request.user.is_authenticated:
        tweets = Tweet.objects.all().order_by("-created_at")
        context = {
            "title": "Home",
            "tweets": tweets
            if (request.GET.get("filter") == "all")
            else tweets.filter(author=request.user),
        }

        return render(request, "core/home.html", context)

    return redirect(reverse("login"))


def profile(request):
    context = {"title": "Profile"}

    return render(request, "core/profile.html", context)


def hashtag(request):
    context = {"title": "Hashtag"}

    if request.GET.get("tag"):
        context["tweets"] = Tweet.objects.filter(body__contains=request.GET.get("tag"))

        return render(request, "core/hashtag.html", context)
    else:
        tweets_hashtags = [t for t in Tweet.objects.all() if t.contains_hashtags()]
        hashtags = []

        for tweet in tweets_hashtags:
            hashtags.extend(tweet.get_hashtags())

        hashtags = list(set(hashtags))
        context["hashtags"] = hashtags

        return render(request, "core/hashtag.html", context)
