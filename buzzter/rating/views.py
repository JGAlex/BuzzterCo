# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from django.contrib.auth.models import User
from posts.models import Post
from models import Rating
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


__author__="JGalex"
__date__ ="$10/11/2013 04:21:23 PM$"


@login_required
def RatingView(request, postID, valor):
	try:
		usuario = request.user
		rate = valor
		publicacion = Post.objects.get(id = postID)

		rate = Rating(usuario=usuario.profile, rate=rate, publicacion=publicacion)		
		publicacion.set_rate(valor)
		rate.save()
			
	except Post.DoesNotExist:
		raise Http404
	
	return HttpResponseRedirect('/Posts/'+postID)
	
	