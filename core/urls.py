from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    path('',views.home,name='home'),
    path('generator',views.generator,name='generator'),
    path('generate-password',views.password, name = 'password'),
    path('greibach',views.greibach,name='greibach'),
    path('greibach-convert',views.greibach, name = 'greibach-convert'),
    path('chomsky',views.chomsky,name='chomsky'),
    path('chomsky-convert',views.chomsky, name = 'chomsky-convert'), 

]
urlpatterns += staticfiles_urlpatterns()