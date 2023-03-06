from django.urls import path
from django.conf import settings
from .views import home, generator, password, Signup
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('',home,name='home'),
    path('home',home,name='home'),
    path('generator',generator,name='generator'),
    path('generate-password',password, name = 'password'),
    path('signup',Signup.as_view(),name='signup'),
    path('signin',LoginView.as_view(template_name='registration/signin.html'),name='signin'),
    path('logout',LogoutView.as_view(),name='logout'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
