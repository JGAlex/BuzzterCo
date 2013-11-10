# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="KarenM"
__date__ ="$20-oct-2013 19:54:14$"

from django import forms
from posts.models import Post, Comments
from django.contrib.comments.forms import CommentForm
from django.db import models

class formPost(forms.ModelForm):
    class Meta:
        model = Post
        fields=['titulo','link','linkImagen','descripcion','tags']
    
class formComments(forms.ModelForm):
    class Meta: 
        model = Comments
        fields=['comentario']