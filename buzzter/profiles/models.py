from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Perfil(User):
    usuario = models.ForeingKey(User, unique=True)
    nombre = models.CharField(max_length=300, blank=True)
    fotografia = models.CharField(max_length=500, blank=True)
    