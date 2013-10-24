# Create your views h
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from posts.models import Post,PostType
from django.views.generic import CreateView
from posts.forms import newPostForm
from django.forms.models import modelform_factory
import pdb
def PostView(request, title):
    
    try:
        post = Post.objects.get(titulo=title)
        autor = post.usuario.usuario
    except Post.DoesNotExist:
        raise Http404
    return render(request, "posts/Post.html",{'post':post,'autor':autor})

@login_required
def now(request):
    return render(request,"posts/newPost.html")

@login_required
def newPost(request,tipo_p):
    tipos = PostType.objects.get(tipo=tipo_p)
    nuevo = Post(usuario=request.user.profile, tipoPublicacion=tipos)
    if request.POST:  
        request.POST['usuario']=request.user.profile
        request.POST['tipoPublicacion']=tipos
        tipoForm = newPostForm(request.POST)        
        if tipoForm.is_valid():
            tipoForm.save()
            return HttpResponseRedirect('/Now/')
    else:
        tipoForm=modelform_factory(form=newPostForm,model=Post, fields=tipos.getFields())
        tipoForm.instance = nuevo
    return render(request,"posts/newPost.html",{'form':tipoForm, 'tipo':tipos})