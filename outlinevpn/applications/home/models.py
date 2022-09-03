from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.

class Producto(models.Model):
    title = models.CharField('Titulo',max_length=50)
    precio = models.IntegerField('Precio')
    descripcion = RichTextUploadingField('Descripcion')
    

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.title


class Principal(TimeStampedModel):
    
    title = models.CharField('Titulo', max_length=25)
    cuerpo = models.CharField('Cuerpo', max_length=300)
    btn = models.CharField('Boton', max_length=20)
    

    class Meta:
        verbose_name = 'Principal'
        verbose_name_plural = 'Principales'

    def __str__(self):
        return self.title


class FAQ(models.Model):
    pregunta = models.CharField('Pregunta', max_length=200)
    respuesta = RichTextUploadingField('Respuesta')
    

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.pregunta




