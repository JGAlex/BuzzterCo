
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
    Modificado: 24/10/13
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
  Modificado: 10/11/13 12:41
  """   
   
  usuario = models.ForeignKey(Profile, related_name='posts')
  tipoPublicacion = models.ForeignKey(PostType)  
  rating = models.FloatField(blank=True, null=True,default=0)  
  fecha = models.DateTimeField(auto_now=True)
  titulo = models.CharField(max_length=50, blank=False, unique=True)
  tags = models.CharField(max_length=1500)  
  link = models.URLField(max_length=350,blank=False,null=False)
  linkImagen = models.URLField(max_length=350,blank=False,null=False)
  descripcion = models.TextField(blank=False)
  
  def set_titulo(self,titulo):
      self.titulo = titulo.replace(" ","_")
      return self.titulo
  
  def get_titulo(self,):
      return self.titulo.replace("_"," ")
  
  def __unicode__(self):
      return self.titulo
  
  def get_rate(self):
      rating = 0
      for rate in self.rates.all():
        rating = rating + rate.rate
      return rating

  def isRated(self, usuario):
      rate = self.rates.get(usuario=usuario)
      return rate

  
  def set_rate (self, rating):
    prom = float(self.get_rate()) + float(rating)
    
    if float(self.rates.count()) != 0:
      prom = round(prom / float(self.rates.count()), 2)
    else:
      prom = 1.0

    self.rating = prom
    self.save()

    return self
  
class Comments(models.Model):
    usuario = models.ForeignKey(Profile,related_name="comentarios")
    fecha = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, related_name="comentarios")
    comentario = models.TextField(blank=False);
    