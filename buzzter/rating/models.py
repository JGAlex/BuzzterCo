# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="JGalex"
__date__ ="$10/11/2013 04:30:44 PM$"

from django.db import models
from profiles.models import Profile
from posts.models import Post

class Rating(models.Model):
	'''
	Esta clase representa el valor con el que un usuario
	calificara una publicacion hecha
	date: 10/11/2013 16:41
	author: Jorge
	branch: JGBranch
	'''
	
	usuario = models.ForeignKey(Profile, related_name="rates")
	rate = models.PositiveIntegerField(blank=True, null=True, default=0)
	publicacion = models.ForeignKey(Post, related_name='rates')