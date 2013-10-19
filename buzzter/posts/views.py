# Create your views here.

from django.http import Http404
from django.shortcuts import render 
from posts.models import Post
from django.views.generic import CreateView


def PostView(request, title):
    
    try:
        post = Post.objects.get(titulo=title)
        autor = post.usuario.usuario
    except Post.DoesNotExist:
        raise Http404
    return render(request, "posts/Post.html",{'post':post,'autor':autor})

class NewPost(CreateView):
    
    from django.core.urlresolvers import reverse_lazy
    
    template_name = "posts/newPost.html"
    model = Post
    success_url = reverse_lazy('newPost')