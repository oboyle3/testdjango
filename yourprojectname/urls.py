"""
URL configuration for yourprojectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import index
from app import views
from app.views import PlayerListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('players/', views.baseball_players, name='baseball_players'),
    path('api/players/', PlayerListAPIView.as_view(), name='player-list'),
    path('caddies/', views.caddies, name='caddies'),
    path('members/', views.members_view, name='members'),
    path('members_tee_times_view/', views.members_tee_times_view, name='members_tee_times_view'),
    path('cources/', views.cources, name='cources'),
]
