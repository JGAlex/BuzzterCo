# Create your views here.
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from messages.models import Messages
from django.views.generic import CreateView
from django.forms.models import modelform_factory
from messages.forms import formMessage
from django.contrib.auth.models import User

@login_required
def SendMessage(request, user_name):
    emisor = request.user
    receptor = User.objects.get(username=user_name)
    mensaje = Messages(emisor=emisor.profile, receptor=receptor.profile)
    mensajes = emisor.profile.enviados.filter(receptor=receptor).order_by('fecha')
    form = formMessage(request.POST or None, instance=mensaje)
    if form.is_valid():
        form.save()
        Http404ResponseRedirect()
    return render(request, 'messages/send.html', {'form':form,'mensajes':mensajes})

