# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Gerson de Leon"
__date__ ="$29/10/2013 10:01:24 AM$"

from django import forms
from messages.models import Messages
from django.db import models

class formMessage(forms.ModelForm ):
     class Meta:
        model = Messages
        fields=['mensaje']
        
        
        