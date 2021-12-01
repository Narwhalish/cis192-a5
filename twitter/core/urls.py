from django.urls import path
from core.views import *

urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path("profile/", profile, name="profile"),
    path("hashtag/", hashtag, name="hashtag"),
]
