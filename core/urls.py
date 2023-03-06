from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("generator", views.generator, name="generator"),
    path("generate-password", views.password, name="password"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
]
urlpatterns += staticfiles_urlpatterns()
