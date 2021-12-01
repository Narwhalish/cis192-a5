from django.http.response import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from core.models import Tweet
from django.contrib.auth import login as _login, authenticate as _authenticate
from django.contrib.auth.models import User

# Create your views here.
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


def home(request):
    if request.method == "POST":
        Tweet.objects.create(
            author=request.user,
            body=request.POST["body"],
        )

        return redirect(reverse("home"))
    context = {"title": "Home", "tweets": Tweet.objects.all()[::-1]}

    return render(request, "core/home.html", context)


def profile(request):
    context = {"title": "Profile"}

    return render(request, "core/profile.html", context)


def hashtag(request):
    context = {"title": "Hashtags"}

    return render(request, "core/hashtag.html", context)
