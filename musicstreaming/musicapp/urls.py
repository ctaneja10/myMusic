from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('signup/', views.creationpage, name='creation'),
    path('handlesignup/', views.handlesignup, name='signup'),
    path('handlelogin/', views.handleLogin, name='login'),
    path('logout/', views.handleLogout, name='handleLogout'),
    path('songs/', views.song_pg, name="songs"),
    path('upload/', views.uploadMusic, name="upload"),
    path('delete/<int:slug>', views.deleteSong, name="delete"),
]