"""tennis_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from tennis_application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^$', views.index, name='index'),
    url(r'^(?P<surface_slug>[\w\-]+)/$', views.show_surface, name='show_surface'),
    url(r'^(?P<surface_slug>[\w\-]+)/(?P<player_name_slug>[\w\-]+)/$', views.show_surface_player, name='show_surface_player'),
    url(r'^$', views.my_view, name='my_view'),
]
