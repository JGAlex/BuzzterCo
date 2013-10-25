# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="KarenM"
__date__ ="$20-oct-2013 19:54:14$"

from django import forms
from posts.models import Post

class formMusic(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo","link","linkImagen",
                  "autor","interprete","album",
                  "tipoGenero","year","descripcion"]
    def save(self, commit=True):
        post = super(formMusic,self).save(commit=False)
        post.set_titulo(self.cleaned_data['titulo'])
        post.link = self.cleaned_data['link']
        post.linkImagen = self.cleaned_data['linkImagen']
        post.autor=self.cleaned_data['autor']
        post.interprete =self.cleaned_data['interprete']
        post.album = self.cleaned_data['album']
        post.tipoGenero = self.cleaned_data['tipoGenero']
        post.year=self.cleaned_data['year']
        post.descripcion = self.cleaned_data['descripcion']
        if commit:
            post.save()
        return post
 

class formMovies(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo","link","linkImagen",
                  "director","tipoGenero","year",
                  "clasificacion","descripcion"]
    def save(self, commit=True):
        post = super(formMusic,self).save(commit=False)
        post.set_titulo(self.cleaned_data['titulo'])
        post.link = self.cleaned_data['link']
        post.linkImagen = self.cleaned_data['linkImagen']
        post.director=self.cleaned_data['director']
        post.tipoGenero = self.cleaned_data['tipoGenero']
        post.year=self.cleaned_data['year']
        post.descripcion = self.cleaned_data['clasificacion']
        post.descripcion = self.cleaned_data['descripcion']
        if commit:
            post.save()
        return post
                  
class formSeries(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo","link","linkImagen",
                  "director","temporada","clasificacion",
                  "tipoGenero","year","descripcion"]
    def save(self, commit=True):
        post = super(formMusic,self).save(commit=False)
        post.set_titulo(self.cleaned_data['titulo'])
        post.link = self.cleaned_data['link']
        post.linkImagen = self.cleaned_data['linkImagen']
        post.director=self.cleaned_data['director']
        post.temporada =self.cleaned_data['temporada']
        post.clasificacion = self.cleaned_data['clasificacion']
        post.tipoGenero = self.cleaned_data['tipoGenero']
        post.year=self.cleaned_data['year']
        post.descripcion = self.cleaned_data['descripcion']
        if commit:
            post.save()
        return post


class formPosters(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo","link","linkImagen",
                  "autor","tipoGenero",
                  "year","descripcion"]

    def save(self, commit=True):
        post = super(formMusic,self).save(commit=False)
        post.set_titulo(self.cleaned_data['titulo'])
        post.link = self.cleaned_data['link']
        post.linkImagen = self.cleaned_data['linkImagen']
        post.autor=self.cleaned_data['autor']
        post.tipoGenero = self.cleaned_data['tipoGenero']
        post.year=self.cleaned_data['year']
        post.descripcion = self.cleaned_data['descripcion']
        if commit:
            post.save()
        return post
                
class formArtBooks(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo","link","linkImagen",
                  "autor","dibujante","clasificacion",
                  "tipoGenero","year","descripcion"]
    def save(self, commit=True):
        post = super(formMusic,self).save(commit=False)
        post.set_titulo(self.cleaned_data['titulo'])
        post.link = self.cleaned_data['link']
        post.linkImagen = self.cleaned_data['linkImagen']
        post.autor=self.cleaned_data['autor']
        post.dibujante =self.cleaned_data['dibujante']
        post.clasificacion = self.cleaned_data['clasificacion']
        post.tipoGenero = self.cleaned_data['tipoGenero']
        post.year=self.cleaned_data['year']
        post.descripcion = self.cleaned_data['descripcion']
        if commit:
            post.save()
        return post
        