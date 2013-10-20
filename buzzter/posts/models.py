
from django.db import models
from profiles.models import Profile
# Create your models here.


class PostType(models.Model):
    
    """
    Esta es una clase que representa
    los distintos tipos de publicaciones 
    que el usuario puede realizar
    Fecha: 20/10/13 16:41
    Autor: Karen (:
    Branch: Branch_Posts
    Modificado:
    """
    
    tipo = models.CharField(max_length=20,blank=False,unique=True)
    
    def __unicode__(self):
        return self.tipo
    
    
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
  tipoPublicacion = models.ForeignKey(PostType)
  
  def __unicode__(self):
      return self.titulo
  
  
