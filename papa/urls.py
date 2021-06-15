from django.urls import include, path
from papa.views import *
from django.contrib import admin
urlpatterns = [
    path('', main_page),
    path('second_page', index2),
    path('auth', authe),
    path('error', authFaild ),
    path('logout',do_log),
    path("registration_form",registration_form),
    path('registration',register),
    path('ajax',ajax),
    path('admin',admin.site.urls),
    path('test',test)
]

