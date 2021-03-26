from django.urls import path

from .views import home,playlist

urlpatterns = [

    path('', home,name= 'home'),
    path('playlist/<int:id>/', playlist, name='playlist')


]