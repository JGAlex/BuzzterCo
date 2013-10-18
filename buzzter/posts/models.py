
from django.db import models
from profiles.models import Profile
# Create your models here.

class Post(models.Model):
  """
  Esta es una clase que representa las 
  publicaciones que el usuario realizara
  Los tipos de campo estan en 
  docs.djangoproject.com/en/dev/ref/models/fields/#field-types
  Fecha: 18/10/13 16:50
  Autor: Karen
  Branch: Karen (local)
  Modificado: 18/10/13 17:03
  """   
  
  titulo = models.CharField(max_length=50, blank=False, unique=True)
  link = models.CharField(max_length=150, blank=True)
  descripcion = models.TextField(blank=False)
  rating = models.PositiveIntegerField()
  eliminar = models.BooleanField()
  linkImagen = models.CharField(max_length=150,blank=False)
  
  usuario = models.ForeignKey(Profile)
  
  def __unicode__(self):
      return self.titulo