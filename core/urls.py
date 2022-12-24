from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    path('',views.home,name='home'),
    path('generator',views.generator,name='generator'),
    path('generate-password',views.password, name = 'password')
    

]
urlpatterns += staticfiles_urlpatterns()