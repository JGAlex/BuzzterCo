from django.db import models
from profiles.models import Profile

class Messages(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    mensaje = models.TextField(blank=False)
    emisor = models.ForeignKey(Profile,related_name="enviados")
    receptor = models.ForeignKey(Profile,related_name= "recibidos")
    