from django.shortcuts import render, redirect
from .forms import RegistrationForm

from .models import Perro, Postulante, Rescatado, Ciudad, Region, TipoVivienda

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request, 'core/home.html')

@login_required(login_url='/ingresar')
def cargar_ciudades(request):
    idre = request.GET.get('region')
    ciudades = Ciudad.objects.filter(idregion=idre).order_by('descripcion')
    return render(request, 'core/formulariopostulante.html', {'ciudades': ciudades})

@login_required(login_url='/ingresar')
def listarPerro(request):
    pe = Perro.objects.all()
    return render(request, 'core/listarperro.html', {'perros': pe})

@login_required(login_url='/ingresar')
def actualizarPerro(request):
    pe = Perro.objects.all()
    mensaje = False
    if request.POST:
        accion = request.POST.get("btnAccion", "")
        if accion == "Buscar":
            idpe = request.POST.get("idperro", "")
            per = Perro.objects.get(idperro=idpe)
            mensaje = False
            return render(request, 'core/actualizarperro.html', {'perros': pe, 'per': per, 'mensaje': mensaje})
        if accion == "Modificar":
            idpe = request.POST.get("idperro", "")
            per = Perro.objects.get(idperro=idpe)
            nombre = request.POST.get("nombre", "")
            raza = request.POST.get("raza", "")
            edad = request.POST.get("edad", "")
            tamano = request.POST.get("tamano", "")
            per.nombre = nombre
            per.raza = raza
            per.edad = edad
            per.tamano = tamano
            per.save()
            mensaje = True
            return render(request, 'core/actualizarperro.html', {'perros': pe, 'mensaje': mensaje})
    return render(request, 'core/actualizarperro.html', {'perros': pe})

@login_required(login_url='/ingresar')
def eliminarPerro(request):
    pe = Perro.objects.all()
    resp = False
    if request.POST:
        idpe = request.POST.get('idperro', "")
        per = Perro.objects.get(idperro=idpe)
        per.delete()
        resp = True
    return render(request, 'core/eliminarperro.html', {'perros': pe, 'respuesta': resp})

@login_required(login_url='/ingresar')
def formularioPerro(request):
    resp = False
    if request.POST:
        idpe = request.POST.get("idperro", "")
        nombre = request.POST.get("nombre", "")
        raza = request.POST.get("raza", "")
        edad = request.POST.get("edad", "")
        tamano = request.POST.get("tamano", "")
        per = Perro(
            idperro=idpe,
            nombre=nombre,
            raza=raza,
            edad=edad,
            tamano=tamano
        )
        per.save()
        resp = True
    return render(request, 'core/formularioperro.html', {'respuesta': resp})

@login_required(login_url='/ingresar')
def listarPostulante(request):
    post = Postulante.objects.all()
    return render(request, 'core/listarpostulante.html', {'postulantes': post})

@login_required(login_url='/ingresar')
def actualizarPostulante(request):
    post = Postulante.objects.all()
    ciud = Ciudad.objects.all()
    regi = Region.objects.all()
    tipo = TipoVivienda.objects.all()
    mensaje = False
    if request.POST:
        accion = request.POST.get("btnAccion", "")
        if accion == "Buscar":
            ru = request.POST.get("rut", "")
            po = Postulante.objects.get(rut=ru)
            mensaje = False
            return render(request, 'core/actualizarpostulante.html', {'postulantes': post, 'po': po, 'ciudades': ciud, 'regiones': regi, 'tipoviviendas': tipo, 'mensaje': mensaje})
        if accion == "Modificar":
            ru = request.POST.get("rut", "")
            po = Postulante.objects.get(rut=ru)
            nom = request.POST.get("nombrecompleto", "")
            fec = request.POST.get("fechanac", "")
            fon = request.POST.get("fono", "")
            cor = request.POST.get("correo", "")
            ciu = request.POST.get("ciudad", "")
            obj_ciudad = Ciudad.objects.get(idciudad=ciu)
            reg = request.POST.get("region", "")
            obj_region = Region.objects.get(idregion=reg)
            tip = request.POST.get("tipovivienda", "")
            obj_tipovivienda = TipoVivienda.objects.get(
                idtipo_vivienda=tip)
            po.nombreCompleto = nom
            po.fechaNac = fec
            po.fono = fon
            po.correo = cor
            po.ciudad = obj_ciudad
            po.region = obj_region
            po.tipoVivienda = obj_tipovivienda
            po.save()
            mensaje = True
            return render(request, 'core/actualizarpostulante.html', {'postulantes': post, 'ciudades': ciud, 'regiones': regi, 'tipoviviendas': tipo, 'mensaje': mensaje})
    return render(request, 'core/actualizarpostulante.html', {'postulantes': post, 'ciudades': ciud, 'regiones': regi, 'tipoviviendas': tipo})

@login_required(login_url='/ingresar')
def eliminarPostulante(request):
    post = Postulante.objects.all()
    resp = False
    if request.POST:
        ru = request.POST.get("rut", "")
        po = Postulante.objects.get(rut=ru)
        po.delete()
        resp = True
    return render(request, 'core/eliminarpostulante.html', {'postulantes': post, 'respuesta': resp})


@login_required(login_url='/ingresar')
def formularioPostulante(request):
    post = Postulante.objects.all()
    ciud = Ciudad.objects.all()
    regi = Region.objects.all()
    tipo = TipoVivienda.objects.all()
    resp = False
    if request.POST:
        ru = request.POST.get("rut", "")
        nom = request.POST.get("nombrecompleto", "")
        fec = request.POST.get("fechanac", "")
        fon = request.POST.get("fono", "")
        cor = request.POST.get("correo", "")
        ciu = request.POST.get("ciudad", "")
        obj_ciudad = Ciudad.objects.get(idciudad=ciu)
        reg = request.POST.get("region", "")
        obj_region = Region.objects.get(idregion=reg)
        tip = request.POST.get("tipovivienda", "")
        obj_tipovivienda = TipoVivienda.objects.get(idtipo_vivienda=tip)
        po = Postulante(
            rut=ru,
            nombreCompleto=nom,
            fechaNac=fec,
            fono=fon,
            correo=cor,
            ciudad=obj_ciudad,
            region=obj_region,
            tipoVivienda=obj_tipovivienda
        )
        po.save()
        resp = True

    return render(request, 'core/formulariopostulante.html', {'postulantes': post, 'ciudades': ciud, 'regiones': regi, 'tipoviviendas': tipo, 'respuesta': resp})

@login_required(login_url='/ingresar')
def listarRescatado(request):
    resc = Rescatado.objects.all()
    return render(request, 'core/listarrescatado.html', {'rescatados': resc})

@login_required(login_url='/ingresar')
def actualizarRescatado(request):
    resc = Rescatado.objects.all()
    per = Perro.objects.all()
    mensaje = False
    if request.POST:
        accion = request.POST.get("btnAccion", "")
        if accion == "Buscar":
            idre = request.POST.get("idrescatado", "")
            re = Rescatado.objects.get(idRescatado=idre)
            mensaje = False
            return render(request, 'core/actualizarrescatado.html', {'rescatados': resc, 'perros': per, 're': re, 'mensaje':mensaje})
        if accion == "Modificar":
            idre = request.POST.get("idrescatado", "")
            re = Rescatado.objects.get(idRescatado=idre)
            fo = request.POST.get("fotografia", "")
            ra = request.POST.get("raza", "")
            de = request.POST.get("descripcion", "")
            es = request.POST.get("estado", "")
            pe = request.POST.get("perro", "")
            obj_perro = Perro.objects.get(idperro=pe)
            re.fotografia = fo
            re.raza = ra
            re.descripcion = de
            re.estado = es
            re.idperro = obj_perro
            re.save()
            mensaje = True
            return render(request, 'core/actualizarrescatado.html', {'rescatados': resc, 'perros': pe, 'mensaje': mensaje})
    return render(request, 'core/actualizarrescatado.html', {'rescatados': resc, 'perros': per})

@login_required(login_url='/ingresar')
def eliminarRescatado(request):
    resc = Rescatado.objects.all()
    resp = False
    if request.POST:
        idr = request.POST.get("idRescatado", "")
        res = Rescatado.objects.get(idRescatado=idr)
        res.delete()
        resp = True
    return render(request, 'core/eliminarrescatado.html', {'rescatados': resc, 'respuesta': resp})


@login_required(login_url='/ingresar')
def formularioRescatado(request):
    per = Perro.objects.all()
    resp = False
    if request.POST:
        idr = request.POST.get("idRescatado", "")
        fo = request.POST.get("fotografia", "")
        ra = request.POST.get("raza", "")
        de = request.POST.get("descripcion", "")
        es = request.POST.get("estado", "")
        pe = request.POST.get("idperro", "")
        obj_perro = Perro.objects.get(idperro=pe)
        resc = Rescatado(
            idRescatado=idr,
            fotografia=fo,
            raza=ra,
            descripcion=de,
            estado=es,
            idperro=obj_perro
        )
        resc.save()
        resp = True
    return render(request, 'core/formulariorescatado.html', {'perros': per, 'respuesta': resp})

def nuevousuario(request):
    if request.method =='POST':
        formulario = RegistrationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/')
    else:
        formulario = RegistrationForm()

    return render(request, 'core/nuevousuario.html', {'formulario': formulario})


#Vistas Usuario normal / visita
@login_required(login_url='/ingresar')
def homeadmin(request):
    return render(request, 'core/homeadmin.html')
@login_required(login_url='/ingresar')
def homeusuario(request):
    return render(request, 'core/homeusuario.html')


# separador
# Autenticacion de usuarios

def ingresar(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_staff:
                    login(request, acceso)
                    return render(request, 'core/homeadmin.html') 
                elif acceso.is_active:
                    return render(request, 'core/homeusuario.html')

                else:
                    return render(request, 'core/noactivo.html')
            else:
                return render(request, 'core/nousuario.html')
    else:
        formulario = AuthenticationForm()
    return render(request, 'core/ingresar.html', {'formulario':formulario})

#-------------------------------------------------------------------------

#Restriccion de usuarios
@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    return render(request, 'core/privado.html', {'usuario':usuario})
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Cierre de sesion
@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Recuperar contraseña
#------------
def password_reset(request):
    return render(request, 'core/password_reset.html')
def password_reset_done(request):
    return render(request, 'core/password_reset_done.html')
def password_reset_confirm(request):
    return render(request, 'core/password_reset_confirm.html')
def password_reset_complete(request):
    return render(request, 'core/password_reset_complete.html')

