# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="t4r0"
__date__ ="$18-oct-2013 18:49:08$"

from django import forms 
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):  
    """
    Representa un formulario para registrarse en el sitio
    Fecha: 18/10/2013 19:47
    Autor: T4r0_o
    Branch: taro
    Modificado: 18/10/2013 
    """
    errorMessages={
        'duplicate_username': "Un usuario con ese nombre ya existe",
    }
    
    username = forms.RegexField(label="Username", max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text="Requerido. 30 caracteres o menos, letras, digitos y los carcateres "
                      "@/./+/-/_ .",
        error_messages={
            'invalid': "puedes usar solo los caraceteres "
                         "@/./+/-/_"})
    password = forms.CharField(label="Password",
        widget=forms.PasswordInput)
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ("username",)
    
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.errorMessages['duplicate_username'],
            code='duplicate_username',
        )
        
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user