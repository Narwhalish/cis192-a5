from django.shortcuts import render

# Create your views here.
def splash(request):
    return render(request, "splash.html", {})


def login(request):
    return render(request, "login.html", {})
