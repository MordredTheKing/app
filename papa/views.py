from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.db import models
from django.http import JsonResponse


def index(request):
    return HttpResponse("Главная страница!")

from papa.models import Person
def index2(request):
    return render(request,'Project.html')
    return HttpResponse(m)
from papa.models import Person

def main_page(request):
    return render(request,'Les1.html')
def authFaild(request):
    return render(request,'error.html')


def authe(request):
    user = authenticate(
        username = request.POST['username'],
        password = request.POST['password']
    )
    if user is None:
        return render(request,'error.html',{})
    else:
        login(request,user)
        return HttpResponseRedirect('/')

def do_log(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("Ты не залогинен")

from papa.models import Client



def register(request):

    password = request.POST["password"]
    password2 = request.POST['password2']
    email2 = request.POST['email']
    login2 = request.POST['login']

    if password != password2:
        return render(request, 'auth.html', {'error_message': 'Passwords do not match.'})
    elif User.objects.filter(username=request.POST['login']).exists():
        return render(request, 'auth.html', {'error_message': 'Login already exists.'})
    elif User.objects.filter(email=request.POST['email']).exists():
        return render(request, 'auth.html', {'error_message': 'Email already exists.'})
    elif email_check(email2) != True:
        return render(request, 'auth.html', {'error_message': 'Enter a valid email address'})
    elif len(login2)<3:
        return render(request, 'auth.html', {'error_message': '3 and more symbols required'})
    else:

        user = User.objects.create_user(
            request.POST["login"],
            password=request.POST["password"],
            email = request.POST['email']

        )
        client = Client(user=user)
        client.save()
        return HttpResponseRedirect('/')


def email_check(email):
    if len(email) > 7 and '@'in email:
        return True


def registration_form(request):
    return render(request,'auth.html')


def ajax(request):

    response = {
        'message': request.POST['login']
    }
    return JsonResponse(response)

def test(request):
    return render(request,'frrg.html')








