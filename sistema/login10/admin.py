from django.contrib import admin
from .models import empleado

# Register your models here.
class Empleadofiltro(admin.ModelAdmin):
    search_fields=['nombre']
    list_filter=('departamento','cargo','sueldo')
    date_hierarchy='fecha'

admin.site.register(empleado,Empleadofiltro)
