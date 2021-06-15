from django.db import models
from django.contrib.auth.models import User
from django import forms
class Person(models.Model):
    type = models.CharField(max_length=100)
    how_many = models.IntegerField(default=0)


class Client(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

# Create your models here.
