from tastypie.resources import ModelResource
from posts.models import PostType, Post, Comments
from tastypie.authorization import DjangoAuthorization
from buzzter.authentication import OAuth20Authentication

class PostTypeResource(ModelResource):
    class Meta:
        queryset = PostType.objects.all()
        resource_name = 'type'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'

class CommentsResource(ModelResource):
    class Meta:
        queryset = Comments.objects.all()
        resource_name = 'comments'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
