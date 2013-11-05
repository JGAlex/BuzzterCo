# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from profiles.forms import SignUpForm, EditUserForm, EditProfileForm
from profiles.models import Profile

def ProfileView(request, user_name):    
    user = User()
    try:
        user = User.objects.get(username = user_name)
        if user == request.user:
            return HttpResponseRedirect('/Me/')
    except User.DoesNotExist:
        raise Http404
    return render(request, 'profiles/profile.html', {'profile':user, 'info':user.profile })

def SignUp(request):
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            perfil = Profile(usuario=user)
            perfil.save()
            return HttpResponseRedirect('/Login/')
        else:
            return render_to_response('profiles/signUp.html',{'form':form}, context_instance=RequestContext(request))
    if request.user.is_authenticated():
        return HttpResponseRedirect('/Now/')
    else:
        form = SignUpForm()
    return render_to_response('profiles/signUp.html',{'form':form}, context_instance=RequestContext(request))
    
@login_required
def editProfile(request):
    userForm = EditUserForm(request.POST or None, instance=request.user)
    profileForm = EditProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            return HttpResponseRedirect('/Now/')
    return render_to_response('profiles/editProfile.html',{'userForm':userForm, 'profileForm':profileForm},
                                    context_instance=RequestContext(request))

def MyPublications(request):
    return render(request, 'profiles/myPublication.html')

def AboutMe(request):
    return render(request, 'profiles/aboutMe.html')

def MyRatings(request):
    return render(request, 'profiles/myRating.html')
            