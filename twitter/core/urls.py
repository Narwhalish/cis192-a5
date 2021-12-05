from django.urls import re_path, path
from core.views import home, login, signup, logout, profile, hashtag


urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path("logout/", logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("hashtag/", hashtag, name="hashtag"),
]
