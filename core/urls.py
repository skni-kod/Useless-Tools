from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import SignIn, SignUp, chomsky, generator, greibach, home, password

urlpatterns = [
    path("", home, name="home"),
    path("home", home, name="home"),
    path("generator", generator, name="generator"),
    path("generate-password", password, name="generate-password"),
    path("signup", SignUp.as_view(), name="signup"),
    path(
        "signin",
        SignIn.as_view(),
        name="signin",
    ),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("reset_password",auth_views.PasswordResetView.as_view(template_name="reset_password/password_reset.html"),name="reset_password"),
    path("reset_sent",auth_views.PasswordResetDoneView.as_view(template_name="reset_password/password_reset_complete.html"),name="password_reset_done"),
    path("reset/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(template_name="reset_password/password_reset_confirm.html"),name="password_reset_confirm"),
    path("reset_password_complete",auth_views.PasswordResetCompleteView.as_view(template_name="reset_password/password_reset_complete.html"),name="password_reset_complete"),
    path("greibach", greibach, name="greibach"),
    path("greibach-convert", greibach, name="greibach-convert"),
    path("chomsky", chomsky, name="chomsky"),
    path("chomsky-convert", chomsky, name="chomsky-convert"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
