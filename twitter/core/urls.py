from django.urls import path
from core.views import *

urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login"),
    path("profile/", profile, name="profile"),
    path("hashtag/", hashtag, name="hashtag"),
]
