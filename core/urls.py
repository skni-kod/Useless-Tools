from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('generator',views.generator,name='generator'),
    path('generate-password',views.password, name = 'password'),
    path('signup',views.signup.as_view(),name='signup'),
    path('signin',LoginView.as_view(template_name='registration/signin.html'),name='signin'),
    path('logout',LogoutView.as_view(),name='logout'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
