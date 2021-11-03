from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Post

class PublicacionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        autor = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Post.objects.create(author = autor, title = 'Titulo publicacion',
                                    text = 'Texto de prueba de la publicación')
        pass


    def test_titulo_label(self):
        publicacion=Post.objects.get(id=1)
        field_label = Post._meta.get_field('text').verbose_name
        self.assertEquals(field_label,'text')

    def test_titulo_max_length(self):
        publicacion=Post.objects.get(id=1)
        max_length = Post._meta.get_field('title').max_length
        self.assertEquals(max_length,100)

    def test_fecha_creacion_label (self):
        publicacion = Post.objects.get(id=1)
        field_label = Post._meta.get_field('created_date').verbose_name
        self.assertEquals(field_label,'Creado')