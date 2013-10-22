# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from profiles.forms import SignUpForm, EditUserForm, EditProfileForm
from profiles.models import Profile

def ProfileView(request, user_name):    
    user = User()
    try:
        user = User.objects.get(username = user_name)
    except User.DoesNotExist:
        raise Http404
    return render(request, 'profiles/profile.html', {'profile':user, 'info':user.profile })

class SignUp(FormView):
    template_name = "profiles/signUp.html"
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        perfil = Profile(usuario = user)
        perfil.save()
        return super(SignUp, self).form_valid(form)
    
@login_required
def editProfile(request):
    if request.POST:
        userForm = EditUserForm(request.POST, instance=request.user)
        profileForm = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            return HttpResponseRedirect('/Now/')
    else:
        userForm = EditUserForm(instance = request.user)
        profileForm = EditProfileForm(instance = request.user.profile)
    return render_to_response('profiles/editProfile.html',{'userForm':userForm, 'profileForm':profileForm},
                                    context_instance=RequestContext(request))
            