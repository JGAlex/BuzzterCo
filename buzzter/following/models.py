from django.db import models
from profiles.models import Profile

class Follower(models.Model):
    """
    Clase para el manejo de los seguidores de un usuario
    Date: 20-10-2013 16:26
    Author: JGalex
    Branch: JGBranch
    """
    
    follower = models.ForeignKey(Profile)
    usuario = models.ForeignKey(Profile, related_name = "seguidores")
    
    def __unicode__(self):
        return self.follower

class Following(models.Model):
    """
    Clase para el manejo de los usuarios que se siguen
    Date: 20-10-2013 17:15
    Author: JGalex
    Branch: JGBranch
    """
    
    following = models.ForeignKey(Profile)
    usuario = models.ForeignKey(Profile, related_name = "siguiendo")
    
    def __unicode__(self):
        return self.following
# Create your models here.
