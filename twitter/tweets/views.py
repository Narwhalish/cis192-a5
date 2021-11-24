from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "login.html", {})


def home(request):
    return render(request, "home.html", {})


def profile(request):
    return render(request, "profile.html", {})


def hashtag(request):
    return render(request, "hashtag.html", {})
