from django.contrib import admin
from papa.models  import Client
from papa.models  import Cat,Expense,Category,Project


admin.site.register(Client)
admin.site.register(Cat)
admin.site.register(Expense)
admin.site.register(Category)
admin.site.register(Project)
# Register your models here.
