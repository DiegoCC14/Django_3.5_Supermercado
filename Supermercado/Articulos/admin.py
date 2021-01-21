from django.contrib import admin

# Register your models here.

from .models import Productos_Supermercado

class MyModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Productos_Supermercado, MyModelAdmin)
