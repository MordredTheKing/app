"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('',include('papa.urls')),
    path('second_page',include('papa.urls')),
    path('auth',include('papa.urls')),
    path('error', include('papa.urls')),
    path('logout', include('papa.urls')),
    path('registration_form', include('papa.urls')),
    path('registration', include('papa.urls')),
    path('ajax',include('papa.urls')),
    path('admin/',include('papa.urls')),
    path('test',include('papa.urls'))
]
