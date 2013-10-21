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
    Modificado: 20/10/13
    """
    
    titulo = forms.CharField(max_length=50)
    link = forms.URLField()
    descripcion = forms.CharField()
    linkImagen = forms.URLField()
    class Meta:
        model = Post
        def save(self, commit=True):
            posts = super(newPostForm, self).save(commit=False)
            posts.titulo=self.cleaned_data["titulo"] 
            posts.link=self.cleaned_data["link"]
            posts.descripcion=self.cleaned_data["descripcion"]
            posts.linkImagen=self.cleaned_data["linkImagen"]
            if commit:
                posts.save()
            return posts