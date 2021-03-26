from django.urls import path

from .views import home,search,about

urlpatterns = [

    path('', home,name= 'home'),
    path('search/', search, name='search'),
    path('search/<data>/', search, name='search'),
    path('about/', about, name='about')

]