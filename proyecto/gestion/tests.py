from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Autor, Libro


@override_settings(
    ALLOWED_HOSTS=['testserver', 'localhost', '127.0.0.1'],
    SECURE_SSL_REDIRECT=False,
)
class GestionSmokeTests(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(
            nombre='Gabriel Garcia Marquez',
            correo='gabo@example.com',
            nacionalidad='Colombiana',
            fecha_nacimiento='1927-03-06',
            biografia='Autor de prueba',
        )
        self.libro = Libro.objects.create(
            titulo='Cien Anos de Soledad',
            fecha_publicacion='1967-05-30',
            genero='Novela',
            isbn='1234567890',
            autor=self.autor,
        )

    def test_lista_autores(self):
        response = self.client.get(reverse('lista_autores'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.autor.nombre)

    def test_inicio_redirige_a_autores(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], reverse('lista_autores'))

    def test_crear_autor(self):
        response = self.client.post(
            reverse('crear_autor'),
            {
                'nombre': 'Isabel Allende',
                'correo': 'isabel@example.com',
                'nacionalidad': 'Chilena',
                'fecha_nacimiento': '1942-08-02',
                'biografia': 'Otra autora',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Autor.objects.filter(correo='isabel@example.com').exists())

    def test_editar_autor(self):
        response = self.client.post(
            reverse('editar_autor', args=[self.autor.pk]),
            {
                'nombre': 'Gabo',
                'correo': 'gabo@example.com',
                'nacionalidad': 'Colombiana',
                'fecha_nacimiento': '1927-03-06',
                'biografia': 'Actualizado',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.autor.refresh_from_db()
        self.assertEqual(self.autor.nombre, 'Gabo')

    def test_eliminar_autor(self):
        autor = Autor.objects.create(
            nombre='Temporal',
            correo='temporal@example.com',
            nacionalidad='Colombiana',
            fecha_nacimiento='1990-01-01',
            biografia='Temporal',
        )
        response = self.client.post(reverse('eliminar_autor', args=[autor.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Autor.objects.filter(pk=autor.pk).exists())

    def test_lista_libros(self):
        response = self.client.get(reverse('lista_libros'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.libro.titulo)

    def test_crear_libro(self):
        response = self.client.post(
            reverse('crear_libro'),
            {
                'titulo': 'El Otono del Patriarca',
                'fecha_publicacion': '1975-01-01',
                'genero': 'Novela',
                'isbn': '1234567891',
                'autor': self.autor.pk,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Libro.objects.filter(isbn='1234567891').exists())

    def test_editar_libro(self):
        response = self.client.post(
            reverse('editar_libro', args=[self.libro.pk]),
            {
                'titulo': 'Cien Anos',
                'fecha_publicacion': '1967-05-30',
                'genero': 'Novela',
                'isbn': '1234567890',
                'autor': self.autor.pk,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.libro.refresh_from_db()
        self.assertEqual(self.libro.titulo, 'Cien Anos')

    def test_eliminar_libro(self):
        libro = Libro.objects.create(
            titulo='Temporal',
            fecha_publicacion='2000-01-01',
            genero='Ensayo',
            isbn='9999999999',
            autor=self.autor,
        )
        response = self.client.post(reverse('eliminar_libro', args=[libro.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Libro.objects.filter(pk=libro.pk).exists())
