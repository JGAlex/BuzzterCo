# Create your views here.
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from messages.models import Messages
from django.views.generic import CreateView
from django.forms.models import modelform_factory
from messages.forms import formMessage
from django.contrib.auth.models import User
from django.db.models import Q

@login_required
def sendMessage(request, user_name):
    try:
        emisor = request.user
        receptor = User.objects.get(username=user_name)
        mensaje = Messages(emisor=emisor.profile, receptor=receptor.profile)
        mensajes = Messages.objects.filter(Q(emisor=receptor.profile, receptor=emisor.profile)|Q(emisor=emisor.profile, receptor=receptor.profile)).order_by('fecha')[:10]
        form = formMessage(request.POST or None, instance=mensaje)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Messages/'+receptor.username+'/')
    except User.DoesNotExist:
        raise Http404
    return render(request, 'messages/send.html', {'form':form,'mensajes':mensajes.all()})
    
        
    
@login_required
def viewAll(request):
    mensajes = request.user.profile.recibidos.all()
    return render(request, 'messages/all.html',{'mensajes':mensajes})
