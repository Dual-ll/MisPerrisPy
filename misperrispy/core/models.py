from django.db import models

# Create your models here.


class Region(models.Model):
    idregion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class TipoVivienda(models.Model):
    idtipo_vivienda = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class Usuario(models.Model):
    idusuario = models.AutoField(max_length=10, primary_key=True)
    usuario = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.usuario


class Ciudad(models.Model):
    idciudad = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    idregion = models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self):
        return self.descripcion


class Perro(models.Model):
    idperro = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    tamano = models.IntegerField()

    def __str__(self):
        return self.nombre


class Postulante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombreCompleto = models.CharField(max_length=100)
    fechaNac = models.DateField(auto_now=False, auto_now_add=False)
    fono = models.IntegerField()
    correo = models.EmailField(max_length=200)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    tipoVivienda = models.ForeignKey(TipoVivienda, on_delete=models.PROTECT)

    def __str__(self):
        return self.rut


class Rescatado(models.Model):
    idRescatado = models.AutoField(
        max_length=10, primary_key=True, blank=False)
    fotografia = models.ImageField(blank=False)
    raza = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=100, blank=False)
    estado = models.CharField(max_length=20, blank=False)
    idperro = models.ForeignKey(Perro, on_delete=models.CASCADE)

