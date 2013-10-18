# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    """
    Esta clase representa el modelo de los perfiles que se utilizarán
    Fecha: 16/10/2013 19:14
    Autor: T4r0_o
    Branch: master
    Modificado: 16/10/2013 19:14
    """
    usuario = models.ForeignKey(User, unique=True)
    nombre = models.CharField(max_length=300, blank=True)
    fotografia = models.ImageField(upload_to="users")
    
    def __unicode__(self):
        return self.usuario.get_username()
        