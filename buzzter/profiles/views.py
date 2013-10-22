# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from profiles.models import Profile
from forms import EditForm
from django.core.context_processors import csrf
def ProfileView(request, user_name):    
    user = User()
    try:
        user = User.objects.get(username = user_name)
    except User.DoesNotExist:
        raise Http404
    return render(request, 'profiles/profile.html', {'profile':user, 'info':user.profile })
def EditView(request):
    if request.POST:
        form = EditForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Edit')
    else:
        form = EditForm()
    args = {}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('profiles/editProfile.html', args)

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