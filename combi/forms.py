
from django import forms
from .models import Reserva


class Consulta_frm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ('nombre', 'telefono','fecha',
                'subeEn', 'bajaEn', 'asiento',
                'pago')
