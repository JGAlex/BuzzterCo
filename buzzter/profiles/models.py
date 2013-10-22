# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from countries.models import Country
# Create your models here.
class Profile(models.Model):
    """
    Esta clase representa el modelo de los perfiles que se utilizarán
    Fecha: 16/10/2013 19:14
    Autor: T4r0_o
    Branch: master
    Modificado: 18/10/2013 
    """
    usuario = models.OneToOneField(User, related_name='profile')
    pais = models.ForeignKey(Country,  null=True)
    fotografia = models.ImageField(upload_to="users", null=True, blank=True,
                                default='users/default.png')    
    followers = models.ManyToManyField(User, related_name='followers', null=True, blank=True)
    followings = models.ManyToManyField(User, related_name='follwings', null=True, blank=True)
    
    def __unicode__(self):
        return self.usuario.get_username()
    
    def isFollowing(self,usuario):
        return bool(self.followings.get(username=usuario.username))