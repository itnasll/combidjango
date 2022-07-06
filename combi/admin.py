from django.contrib import admin

from combi.models import Lugar, Reserva

class reservaAdm(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'fecha', 'subeEn', 'bajaEn')
    list_filter = ('nombre', 'fecha')
    search_fields = ('nombre', 'telefono', 'subeEn','bajaEn')

# Register your models here.
admin.site.register (Lugar)
admin.site.register (Reserva, reservaAdm) 