from django.shortcuts import render
from .models import Perro, Postulante, Rescatado, Ciudad, Region, TipoVivienda
# Create your views here.


def index(request):
    return render(request, 'core/home.html')


def cargar_ciudades(request):
    idre = request.GET.get('region')
    ciudades = Ciudad.objects.filter(idregion=idre).order_by('descripcion')
    return render(request, 'core/formulariopostulante.html', {'ciudades': ciudades})


def listarPerro(request):
    pe = Perro.objects.all()
    return render(request, 'core/listarperro.html', {'perros': pe})


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


def eliminarPerro(request):
    pe = Perro.objects.all()
    resp = False
    if request.POST:
        idpe = request.POST.get('idperro', "")
        per = Perro.objects.get(idperro=idpe)
        per.delete()
        resp = True
    return render(request, 'core/eliminarperro.html', {'perros': pe, 'respuesta': resp})


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


def listarPostulante(request):
    post = Postulante.objects.all()
    return render(request, 'core/listarpostulante.html', {'postulantes': post})


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


def eliminarPostulante(request):
    post = Postulante.objects.all()
    resp = False
    if request.POST:
        ru = request.POST.get("rut", "")
        po = Postulante.objects.get(rut=ru)
        po.delete()
        resp = True
    return render(request, 'core/eliminarpostulante.html', {'postulantes': post, 'respuesta': resp})


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


def listarRescatado(request):
    resc = Rescatado.objects.all()
    return render(request, 'core/listarrescatado.html', {'rescatados': resc})


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


def eliminarRescatado(request):
    resc = Rescatado.objects.all()
    resp = False
    if request.POST:
        idr = request.POST.get("idRescatado", "")
        res = Rescatado.objects.get(idRescatado=idr)
        res.delete()
        resp = True
    return render(request, 'core/eliminarrescatado.html', {'rescatados': resc, 'respuesta': resp})


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
