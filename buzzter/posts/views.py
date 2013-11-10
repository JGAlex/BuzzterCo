# Create your views h
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from posts.models import Post,PostType,Comments
from django.views.generic import CreateView
from posts import forms as PostForms
from django.forms.models import modelform_factory


def PostView(request, title):    
    try:
        post = Post.objects.get(titulo=title)
        autor = post.usuario.usuario
        comentarios = []
        if request.user.is_authenticated():
            comentarios = Comments.objects.filter(post=post).all()
            comentario = Comments(usuario=request.user.profile,post=post)
            form = PostForms.formComments(request.POST or None,instance=comentario)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/Posts/'+title+'/')
    except Post.DoesNotExist:
        raise Http404
    return render(request, "posts/Post.html",{'post':post,'autor':autor,'form':form,'comments':comentarios})

@login_required
def now(request):
    listpost = Post.objects.all()[:8]
    return render(request,"posts/newPost.html",{"posts": listpost})

@login_required
def newPostMusic(request):
    tipos = PostType.objects.get(tipo='Music')
    nuevo = Post(usuario=request.user.profile, tipoPublicacion=tipos)
    tipoForm = PostForms.formMusic(request.POST or None, instance=nuevo)
    
    if tipoForm.is_valid():
        tipoForm.save()
        return HttpResponseRedirect('/Now/')
    return render(request,"posts/newPostForm.html",{'form':tipoForm})

@login_required
def newPostMovies(request):
    tipos = PostType.objects.get(tipo='Movies')
    nuevo = Post(usuario=request.user.profile, tipoPublicacion=tipos)
    tipoForm = PostForms.formMovies(request.POST or None, instance=nuevo)
    
    if tipoForm.is_valid():
        tipoForm.save()
        return HttpResponseRedirect('/Now/')
    return render(request,"posts/newPostForm.html",{'form':tipoForm})

@login_required
def newPostSeries(request):
    tipos = PostType.objects.get(tipo='Series')
    nuevo = Post(usuario=request.user.profile, tipoPublicacion=tipos)
    tipoForm = PostForms.formSeries(request.POST or None, instance=nuevo)
    
    if tipoForm.is_valid():
        tipoForm.save()
        return HttpResponseRedirect('/Now/')
    return render(request,"posts/newPostForm.html",{'form':tipoForm})

@login_required
def newPostPosters(request):
    tipos = PostType.objects.get(tipo='Posters')
    nuevo = Post(usuario=request.user.profile, tipoPublicacion=tipos)
    tipoForm = PostForms.formPosters(request.POST or None, instance=nuevo)
    
    if tipoForm.is_valid():
        tipoForm.save()
        return HttpResponseRedirect('/Now/')
    return render(request,"posts/newPostForm.html",{'form':tipoForm})

@login_required
def newPostArtBooks(request):
    tipos = PostType.objects.get(tipo='ArtBooks')
    nuevo = Post(usuario=request.user.profile, tipoPublicacion=tipos)
    tipoForm = PostForms.formArtBooks(request.POST or None, instance=nuevo)
    
    if tipoForm.is_valid():
        tipoForm.save()
        return HttpResponseRedirect('/Now/')
    return render(request,"posts/newPostForm.html",{'form':tipoForm})