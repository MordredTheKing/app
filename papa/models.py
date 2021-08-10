from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils.text import slugify

class Person(models.Model):
    type = models.CharField(max_length=100)
    how_many = models.CharField(max_length=90, db_index=True)

class Client(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()



# ____
# class Finance(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, unique=True,blank=True)
#     budget = models.IntegerField()
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Finance, self).save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True,blank=True)
    budget = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    @property
    def budget_left(self):
        expense_list = Expense.objects.filter(project=self)
        total_expense_amount = 0
        for expense in expense_list:
            total_expense_amount += expense.amount

        # temporary solution, because the form currently only allows integer amounts
        total_expense_amount = int(total_expense_amount)

        return self.budget + total_expense_amount

    @property
    def total_transactions(self):
        expense_list = Expense.objects.filter(project=self)
        return len(expense_list)



class Category(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class Expense(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # class Meta:
    #     ordering = ('-amount',)