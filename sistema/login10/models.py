from django.db import models

# Create your models here.
class empleado(models.Model):
    nombre = models.CharField(max_length=60, blank=False, null=False)
    departamento = models.CharField(max_length=50, blank=False, null=False)
    cargo = models.CharField(max_length=70, blank=False, null=False )
    sueldo = models.PositiveIntegerField()
    fecha = models.DateField()
    
    def __str__(self):
        return f'{self.nombre}, {self.cargo}, {self.departamento}'