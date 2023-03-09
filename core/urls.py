from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import home, generator, password, greibach, chomsky, Signup


urlpatterns = [
    path("", home, name="home"),
    path("home", home, name="home"),
    path("generator", generator, name="generator"),
    path("generate-password", password, name="password"),
    path("signup", Signup.as_view(), name="signup"),
    path(
        "signin",
        LoginView.as_view(template_name="registration/signin.html"),
        name="signin",
    ),
    path("logout", LogoutView.as_view(), name="logout"),
    path('greibach',greibach,name='greibach'),
    path('greibach-convert',greibach, name = 'greibach-convert'),
    path('chomsky',chomsky,name='chomsky'),
    path('chomsky-convert',chomsky, name = 'chomsky-convert'), 

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
