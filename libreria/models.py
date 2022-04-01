from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100,verbose_name='Titulo')
    imagen = models.ImageField(upload_to = 'imagenes/',null= True,verbose_name='Imagen')
    description = models.TextField(verbose_name='Description',null=True)