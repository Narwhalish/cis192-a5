from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from core.models import Tweet

# Create your views here.
def login(request):
    context = {"title": "Login"}

    return render(request, "core/login.html", context)


def home(request):
    if request.method == "POST":
        Tweet.objects.create(
            author=request.user,
            title=request.POST["title"],
            body=request.POST["body"],
        )

        return HttpResponseRedirect(reverse("home"))
    else:
        context = {"title": "Home", "tweets": Tweet.objects.all()}

        return render(request, "core/home.html", context)


def profile(request):
    context = {"title": "Profile"}

    return render(request, "core/profile.html", context)


def hashtag(request):
    context = {"title": "Hashtags"}

    return render(request, "core/hashtag.html", context)
