from django.urls import path
from .views import home, generator, password, greibach, chomsky
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    path('',home,name='home'),
    path('generator',generator,name='generator'),
    path('generate-password',password, name = 'password'),
    path('greibach',greibach,name='greibach'),
    path('greibach-convert',greibach, name = 'greibach-convert'),
    path('chomsky',chomsky,name='chomsky'),
    path('chomsky-convert',chomsky, name = 'chomsky-convert'), 

]
urlpatterns += staticfiles_urlpatterns()