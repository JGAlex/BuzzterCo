# -*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import render
from django.views.generic import CreateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from profiles.models import Profile

def ProfileView(request, user_name):    
    user = User()
    try:
        user = User.objects.get(username = user_name)
    except User.DoesNotExist:
        raise Http404
    return render(request, 'profiles/profile.html', {'profile':user, 'info':user.profile })

class EditProfile(CreateView):
    
    template_name = 'profiles/editProfile.html'
    model = Profile
    success_url = reverse_lazy('profile')

class SignUp(FormView):
    from profiles.forms import SignUpForm
    from profiles.models import Profile
    template_name = "profiles/signUp.html"
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        perfil = Profile(usuario = user)
        perfil.save()
        return super(SignUp, self).form_valid(form)