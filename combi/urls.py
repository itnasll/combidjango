from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.current_datetime, name='current_datetime'),
    path('home/', views.home, name='casa' ),
    path('reserva/', views.reserva, name='new_reserva'),
    path('listado/', views.listado, name='lista'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('buscar/', views.buscar, name='buscar'),
]
