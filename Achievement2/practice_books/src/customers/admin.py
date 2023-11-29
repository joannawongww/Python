from django.contrib import admin

# Register your models here.

# import class
from .models import Customer

# register class
admin.site.register(Customer)
