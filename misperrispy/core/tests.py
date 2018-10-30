from django.test import TestCase
from .models import Perro


class TestPostulante(TestCase):

    @classmethod
    def setUpTestData(cls):
        Perro.objects.create(idperro=10, nombre="Laika",
                             raza="Pastor Aleman", edad=6, tamano=45)

    def test_first_name_label(self):
        perro = Perro.objects.get(idperro=10)
        campo = perro._meta.get_field('nombre').verbose_name
        self.assertEqual(campo, 'nombre')

    def test_raza_coincide(self):
        perro = Perro.objects.get(idperro=10)
        campo = perro._meta.get_field('raza').verbose_name
        self.assertEqual(campo, 'raza')

    def test_edad_coincide(self):
        perro = Perro.objects.get(idperro=10)
        campo = perro._meta.get_field('edad').verbose_name
        self.assertEqual(campo, 'edad')

    def test_first_name_max_length(self):
        perro = Perro.objects.get(idperro=10)
        max_length = perro._meta.get_field('raza').max_length
        self.assertEqual(max_length, 100)
