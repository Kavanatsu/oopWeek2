from django.contrib import admin

from catalog.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Category)
