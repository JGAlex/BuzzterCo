# Create your views h
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from posts.models import Post,PostType,Comments
from django.views.generic import CreateView
from posts import forms as PostForms
from django.forms.models import modelform_factory


def PostView(request, id):    
    try:
        post = Post.objects.get(id=id)
        autor = post.usuario.usuario
        comentarios = []
        if request.user.is_authenticated():
            comentarios = Comments.objects.filter(post=post).all()
            comentario = Comments(usuario=request.user.profile,post=post)
            form = PostForms.formComments(request.POST or None,instance=comentario)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/Posts/'+id+'/')
    except Post.DoesNotExist:
        raise Http404
    return render(request, "posts/Post.html",{'post':post,'autor':autor,'form':form,'comments':comentarios})

@login_required
def now(request):
    listpost = Post.objects.order_by('-fecha')[:8]
    return render(request,"posts/now.html",{"posts": listpost})

@login_required
def newPost(request, tipoP):
    tipos = PostType.objects.get(tipo=tipoP)
    nuevo = Post(usuario=request.user.profile, tipoPublicacion=tipos)
    tipoForm = PostForms.formPost(request.POST or None, instance=nuevo)    
    if tipoForm.is_valid():
        tipoForm.save()
        return HttpResponseRedirect('/Now/')
    return render(request,"posts/newPost.html",{'form':tipoForm, 'postUrl':'/Posts/New/'+tipoP+'/'})

@login_required
def deletePost(request , id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
    except Post.DoesNotExist:
        raise Http404
    return HttpResponseRedirect('/Now/')

@login_required
def search_people_posts(request):
    if request.POST:
        textToSeach = request.POST['textToSeach']
    else:
        textToSeach = ''

        #persona = user.objects.filter(username__contains = textToSeach)
        publicacion = Post.objects.filter(titulo__contains = textToSeach)

    return render(request,'postSearch.html', {'publicacion':publicacion})

