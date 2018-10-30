from django.contrib import admin
from django.urls import path, include
from .views import index, cargar_ciudades, formularioPerro, formularioPostulante, formularioRescatado, listarPerro, listarPostulante, listarRescatado, eliminarPerro, eliminarPostulante, eliminarRescatado, actualizarPerro, actualizarPostulante, actualizarRescatado
urlpatterns = [
    path('', index, name='home'),
    path('formulariopostulante', formularioPostulante, name='ingps'),
    path('formularioperro', formularioPerro, name='ingms'),
    path('actualizarpostulante', actualizarPostulante, name='actpo'),
    path('actualizarperro', actualizarPerro, name='actpe'),
    path('listarpostulante', listarPostulante, name='lispo'),
    path('listarperro', listarPerro, name='lispe'),
    path('eliminarperro', eliminarPerro, name='elpe'),
    path('eliminarpostulante', eliminarPostulante, name='elpo'),
    path('ajax/cargar_ciudades', cargar_ciudades, name='ajax_cargar_ciudades'),
    path('formulariorescatado', formularioRescatado, name='resc'),
    path('listarrescatado', listarRescatado, name='lisre'),
    path('actualizarrescatado', actualizarRescatado, name='acture'),
    path('eliminarrescatado', eliminarRescatado, name="elire")
]
