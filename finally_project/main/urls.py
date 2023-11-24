"""
URL configuration for finally_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import *
from django.shortcuts import redirect


urlpatterns = [
    path('logout/' , log_out , name = 'logout'),
    path('register/' , register , name = 'register'),
    path('' , lambda request: redirect('/home')),
    path('home/', base),
    path('telegramm_post/' , Tg_post , name = 'tg_post'),
    path('telegramm/', tg_all, name='tg'),
    path('discord_post/', Ds_post, name='ds_post'),
    path('discord/', ds_all, name='ds'),
    path('tg_reviews_add/', reviews_tg_add , name = 'rev_tg_add'),
    path('tg_reviews/', reviews_tg, name='rev_tg'),
    path('ds_reviews_add/', reviews_ds_add, name='rev_ds_add'),
    path('ds_reviews/', reviews_ds, name='rev_ds'),
]
