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
        fields=['titulo','link','linkImagen','year','descripcion']
    
    def save(self,commit=True):
        post = super(formPost,self).save(commit=False)
        post.set_titulo(self.cleaned_data['titulo'])
        post.link = self.cleaned_data['link']
        post.linkImagen = self.cleaned_data['linkImagen']
        post.year=self.cleaned_data['year']
        post.descripcion = self.cleaned_data['descripcion']
        if commit:
            post.save()
        return post

class formMusic(formPost):
    class Meta:
        model = Post
        fields = ["titulo","link","linkImagen",
                  "autor","interprete","album",
                  "tipoGenero","year","descripcion"]
    def save(self, commit=True):       
        post = super(formMusic,self).save(commit=False)
        post.autor=self.cleaned_data['autor']
        post.interprete =self.cleaned_data['interprete']
        post.album = self.cleaned_data['album']
        post.tipoGenero = self.cleaned_data['tipoGenero']
        if commit:
            post.save()
        return post
 

class formMovies(formPost):
    class Meta:
        model = Post
        fields = ["titulo","link","linkImagen",
                  "director","tipoGenero","year",
                  "clasificacion","descripcion"]
    def save(self, commit=True):
        post = super(formMovies,self).save(commit=False)
        post.director=self.cleaned_data['director']
        post.tipoGenero = self.cleaned_data['tipoGenero']
        post.clasificacion = self.cleaned_data['clasificacion']
        if commit:
            post.save()
        return post
                  
class formSeries(formPost):
    class Meta:
        model = Post
        fields = ["titulo","link","linkImagen",
                  "director","temporada","clasificacion",
                  "tipoGenero","year","descripcion"]
    def save(self, commit=True):
        post = super(formSeries,self).save(commit=False)
        post.director=self.cleaned_data['director']
        post.temporada =self.cleaned_data['temporada']
        post.clasificacion = self.cleaned_data['clasificacion']
        post.tipoGenero = self.cleaned_data['tipoGenero']
        if commit:
            post.save()
        return post


class formPosters(formPost):
    class Meta:
        model = Post
        fields = ["titulo","link","linkImagen",
                  "autor","year","descripcion"]
    def save(self, commit=True):
        post = super(formPosters,self).save(commit=False)
        post.autor=self.cleaned_data['autor']
        if commit:
            post.save()
        return post
                
class formArtBooks(formPost):
    class Meta:
        model = Post
        fields = ["titulo","link","linkImagen",
                  "autor","dibujante","clasificacion",
                  "tipoGenero","year","descripcion"]
    def save(self, commit=True):
        post = super(formArtBooks,self).save(commit=False)
        post.autor=self.cleaned_data['autor']
        post.dibujante =self.cleaned_data['dibujante']
        post.clasificacion = self.cleaned_data['clasificacion']
        post.tipoGenero = self.cleaned_data['tipoGenero']
        if commit:
            post.save()
        return post

class formComments(forms.ModelForm):
    class Meta: 
        model = Comments
        fields=['comentario']