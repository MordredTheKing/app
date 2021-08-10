from django.urls import include, path
from papa.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', main_page),
    path('login',login_page),
    # path('second_page', index2),
    path('auth', authe),
    # path('error', authFaild ),
    path('logout',do_log),
    path("registration",registration_form),
    path('register',register),
    # path('ajax',ajax),
    path('admin',admin.site.urls),
    # path('test',test),
    # path('usd',usd),
    # path('exp', experiment),
    # path('cat',cat),
    # path('finance', finance),
    path('project', project_list, name='list'),
    path('add', ProjectCreateView.as_view(), name='add'),
    path('<slug:project_slug>', project_detail, name='detail')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


