from django.urls import path, re_path, reverse
from core.views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login"),
    re_path(r"^signup/$", RedirectView.as_view(pattern_name="login"), name="signup"),
    path("profile/", profile, name="profile"),
    path("hashtag/", hashtag, name="hashtag"),
]
