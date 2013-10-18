# -*- coding: utf-8 -*-

from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView
from django import forms 

def ProfileView(request, user_name):
    try:
        user = User.objects.get(username = user_name)
    except User.DoesNotExist:
        raise Http404
    return render(request, 'profiles/profile.html', {'profile':user})

class EditProfile(CreateView):
    
    from profiles.models import Profile
    from django.core.urlresolvers import reverse_lazy
    
    template_name = 'profiles/editProfile.html'
    model = Profile
    success_url = reverse_lazy('profile')