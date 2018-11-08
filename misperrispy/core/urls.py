from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from . import views
from .views import index, cargar_ciudades, formularioPerro, formularioPostulante, formularioRescatado, listarPerro, listarPostulante, listarRescatado, eliminarPerro, eliminarPostulante, eliminarRescatado, actualizarPerro, actualizarPostulante, actualizarRescatado, nuevousuario, homeadmin, homeusuario, ingresar, cerrar, privado, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

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
    path('eliminarrescatado', eliminarRescatado, name="elire"),
    path('homeadmin', homeadmin, name="homa"),
    path('homeusuario', homeusuario, name="serv"),
    path('nuevousuario', nuevousuario, name="newu"),
    path('ingresar', ingresar, name="ingr"),
    path('cerrar', cerrar, name="cerr"),
    path('privado', privado, name="priv"),
    path('reset/password_reset', password_reset, {'return render(request)':'core/password_reset_form.html','email_template_name':'core/password_reset_email.html'}, name="password_reset"),
    path('reset/password_reset_done', password_reset_done, {'template_name':'core/password_reset_done.html'}, name="password_reset_done"),
    path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name':'core/password_reset_confirm.html'}, name="password_reset_confirm"),
    path('reset/done', password_reset_complete, {'template_name':'core/password_reset_complete.html'}, name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
