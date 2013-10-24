# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="KarenM"
__date__ ="$20-oct-2013 19:54:14$"

from django import forms
from posts.models import Post

class newPostForm(forms.ModelForm):
    """
    Esta clase es para el formulario para 
    una nueva publicacion 
    Fecha: 20/10/13 19:56
    Autor: Karen
    Branch: Branch_Post
    Modificado: 23/10/13
    """
    def __init__(self,*args,**kwargs):
        super(newPostForm, self).__init__(*args,**kwargs)
        for campo in self.fields.values():
            campo.required = False

    class Meta:
        model = Post
 
    