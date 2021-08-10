from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.db import models
from django.http import JsonResponse
import pickle
from pymemcache import Client
from papa.models import Person


def index(request):
    return HttpResponse("Главная страница!")

from papa.models import Person
def index2(request):
    return render(request,'Project.html')
    return HttpResponse(m)
from papa.models import Person

def main_page(request):
    # return render(request,'Les1.html')
    return render(request,'main_page.html')
def login_page(request):
    return render(request,'Login_page.html')
def authFaild(request):
    return render(request,'error.html')


def authe(request):
    user = authenticate(
        username = request.POST['username'],
        password = request.POST['password']
    )
    if user is None:
        return render(request, 'Login_page.html', {'error_message': 'Invalid login or password'})

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
        return render(request, 'Registration.html', {'error_message': 'Passwords do not match.'})
    elif User.objects.filter(username=request.POST['login']).exists():
        return render(request, 'Registration.html', {'error_message': 'Login already exists.'})
    elif User.objects.filter(email=request.POST['email']).exists():
        return render(request, 'Registration.html', {'error_message': 'Email already exists.'})
    elif email_check(email2) != True:
        return render(request, 'Registration.html', {'error_message': 'Enter a valid email address'})
    elif len(login2)<3:
        return render(request, 'Registration.html', {'error_message': '3 and more symbols required'})
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
    return render(request,'Registration.html')

from .models import *
from django.shortcuts import get_object_or_404
from django.utils.text import slugify



def project_list(request):
    project_list = Project.objects.all()
    if request.method == 'DELETE':
        id = json.loads(request.body)['id']
        project = Project.objects.get(id=id)
        project.delete()
    return render(request, 'project-list.html', {'project_list': project_list})
from .forms import ExpenseForm
import json
def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)

    if request.method == 'GET':
        category_list = Category.objects.filter(project=project)
        return render(request, 'project-detail.html', {'project': project, 'expense_list': project.expenses.all(), 'category_list': category_list})

    elif request.method == 'POST':
        # process the form
        form = ExpenseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            category_name = form.cleaned_data['category']

            category = get_object_or_404(Category, project=project, name=category_name)

            Expense.objects.create(
                project=project,
                title=title,
                amount=amount,
                category=category
            ).save()

    elif request.method == 'DELETE':
        id = json.loads(request.body)['id']
        expense = Expense.objects.get(id=id)
        expense.delete()


        return HttpResponse('')

    return HttpResponseRedirect(project_slug)

from django.views.generic import CreateView
class ProjectCreateView(CreateView):
    model = Project
    template_name = 'add-project.html'
    fields = ('name', 'budget')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        categories = self.request.POST['categoriesString'].split(',')
        for category in categories:
            Category.objects.create(
                project=Project.objects.get(id=self.object.id),
                name=category
            ).save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['name'])


def ajax(request):

    response = {
        'message': request.POST['login']
    }
    return JsonResponse(response)

def test(request):
    return render(request,'frrg.html')

import requests
import json
import datetime
from datetime import date

def usd(request):
    data_1 = date.today()
    data_2 = date.today()-datetime.timedelta(days = 7)
    response = requests.get(
    f'https://www.nbrb.by/API/ExRates/Rates/Dynamics/145?startDate={data_2}&endDate={data_1} '
    )
    data = json.loads(response.text)


    return HttpResponse(data)

# bd index

from papa.models import Person
import random
from datetime import datetime

#
# def experiment(request):
#     size = 100000
#     slice_size = 500
#     Person.objects.all().delete()
#     for _ in range(int(size / slice_size)):
#         slice = []
#         for _ in range(slice_size):
#             slice.append(
#                 Person(
#                     type=str(random.randint(1, 1000)),
#                     how_many=str(
#                         random.randint(1,100)
#                     )
#                 )
#             )
#         Person.objects.bulk_create(slice, slice_size)
#
#     sum = 0
#     for _ in range(100):
#         start = datetime.now()
#         list(Person.objects.filter(
#             how_many=random.randint(
#                 1,100
#             )
#         ))
#         delta = (datetime.now() - start).total_seconds()
#         sum = sum + delta
#     print("Время выполнения 100 запрсосов: " +
#           str(sum) + ' секунд')
#     return HttpResponse()
#
#
# from papa.models import Cat
#
# def cat(request):
#     cat = Cat.objects.all()[0]
#     return render(request,'les1.html')
#
