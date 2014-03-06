# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from tastypie.resources import ModelResource
from posts.models import PostType, Post, Comments


class PostTypeResource(ModelResource):
    class Meta:
        queryset = PostType.objects.all()
        resource_name = 'PostTypeResource'

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'PostResource'

class CommentsResource(ModelResource):
    class Meta:
        queryset = Comments.objects.all()
        resource_name = 'CommentsResource'