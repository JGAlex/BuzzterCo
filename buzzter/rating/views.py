# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from django.contrib.auth.models import User
from posts.models import Post
from models import Rating


__author__="JGalex"
__date__ ="$10/11/2013 04:21:23 PM$"



def RatingView(request, postID, valor):
	usuario = request.user
	rate = valor
	publicacion = Post.objects.get(id = postID)

	rate = Rating(usuario=usuario, rate=rate, publicacion=publicacion)
	rate.save()
	return rate

def set_rate (self, rating, publicacion):
	prom = publicacion.rate
	prom = prom / publicacion.rate.count

	return prom