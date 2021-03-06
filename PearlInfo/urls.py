"""PearlInfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from admin1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", views.index),
    path("login/", views.login),
    path("check_login", views.check_login),
    path("dashboard/", views.dashboard),
    path("profile/", views.profile),
    path("logout/", views.logout),
    path("create_user/", views.create_user),
    path("data_stored", views.data_stored),
    path("edit_profile/<int:id>", views.edit_profile),
    path("data_updated/<int:id>", views.data_updated),    
]
