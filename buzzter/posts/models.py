
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
    Modificado: 20/10/13
    """
    
    tipo = models.CharField(max_length=20,blank=False,unique=True)
    
    def __unicode__(self):
        return self.tipo


class Genre(models.Model):
    """
    Esta clase permite representara los distintos generos
    de las publicaciones
    Fecha: 21/10/13 10:40
    Autor: Karen
    Branch: Branch_Post
    Modificado:
    """
    
    genero = models.CharField(max_length=50,blank=True,null=False)    
    tipoGenero = models.ManyToManyField(PostType, related_name="tipoGenero", null=True, blank=True)
    
    def __unicode__(self):
        return self.genero
    
    
class Post(models.Model):
  """
  Esta es una clase que representa las 
  publicaciones que el usuario realizara
  Los tipos de campo estan en 
  docs.djangoproject.com/en/dev/ref/models/fields/#field-types
  Fecha: 18/10/13 16:50
  Autor: Karen
  Branch: Karen (local)
  Modificado: 21/10/13 17:03
  """   
  
  titulo = models.CharField(max_length=50, blank=False, unique=True)
  link = models.URLField(max_length=150, blank=True)
  descripcion = models.TextField(blank=False)
  rating = models.PositiveIntegerField()
  eliminar = models.BooleanField()
  linkImagen = models.URLField(max_length=150,blank=False)
  autor = models.CharField(max_length=50,blank=True, null=True)
  interprete = models.CharField(max_length=50,blank=True, null=True)
  album = models.CharField(max_length=50,blank=True, null=True)
  year = models.PositiveIntegerField()
  director = models.CharField(max_length=50,blank=True, null=True)
  clasificacion = models.CharField(max_length=50,blank=True,null=True)
  dibujante = models.CharField(max_length=50,blank=True, null=True)
  temporada = models.CharField(max_length=50,blank=True, null=True)
  
  
  usuario = models.ForeignKey(Profile)
  tipoPublicacion = models.ForeignKey(PostType)
  tipoGenero = models.ForeignKey(Genre, related_name="tipo_Genero", blank=True, null=True)
  
  def __unicode__(self):
      return self.titulo
  
  
