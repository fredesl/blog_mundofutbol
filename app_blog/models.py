from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='fotos/', null=True, blank=True)
    etiqueta = models.CharField(max_length=30)

    def __str__(self):
        return f"Título: {self.titulo} - Subtitilo: {self.subtitulo} - Autor: {self.autor}"
    

class PerfilAvatar(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='avatars/', null=True, blank=True)

   