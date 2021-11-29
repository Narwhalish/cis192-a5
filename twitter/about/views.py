from django.shortcuts import render

# Create your views here.
def splash(request):
    context = {"title": "About"}

    return render(request, "about/splash.html", context)
