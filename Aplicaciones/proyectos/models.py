from django.db import models
import datetime
# Create your models here.
class Proyecto(models.Model):
    date = models.DateField(primary_key=True, unique=True, default=datetime.date.today)
    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=90)
    descripcion = models.CharField(max_length=2000)
    imagen = models.ImageField(upload_to='proyecto_images/', blank=True, null=True)
    publish = models.BooleanField(default=True)

    def __str__(self):
        texto = "[{0} {1}]"
        if self.publish:
            t_publish = "On"
        else:
            t_publish = "Off"
        return texto.format(t_publish, self.nombre)