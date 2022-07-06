from django.db import models
from django.utils import timezone

# Create your models here.

class Lugar(models.Model):
    nombre = models.CharField(max_length=120)
    codpost = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    nombre = models.CharField(max_length=80)
    telefono  = models.IntegerField()
    fecha = models.DateTimeField(default=timezone.now)  
    subeEn = models.ForeignKey('Lugar', on_delete=models.CASCADE, related_name='subeEn_Lugar')
    bajaEn  = models.ForeignKey('Lugar', on_delete=models.CASCADE, related_name='bajaEn_Lugar')
    asiento  = models.CharField(max_length=3)
    pago  = models.DecimalField(max_digits=6, decimal_places=2)
    

    def __str__(self):
        return self.nombre
