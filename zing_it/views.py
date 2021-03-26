from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



my_playlists=[
        {"id":1,"name":"Car Playlist","numberOfSongs":4},
        {"id":2,"name":"Coding Playlist","numberOfSongs":2}
    ]

def home(request):
    return render(request,'zing_it/home.html',{'my_playlists':my_playlists})

def about(request):
    return render(request,'zing_it/about.html')

def search(request,data):
    context = {'data':data}
    return render(request,'zing_it/search.html',context=context)

