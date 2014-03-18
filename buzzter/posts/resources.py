from tastypie.resources import ModelResource
from posts.models import PostType, Post, Comments
from tastypie.authorization import DjangoAuthorization
from buzzter.authentication import OAuth20Authentication

class PostTypeResource(ModelResource):
    class Meta:
        queryset = PostType.objects.all()
        resource_name = 'type'
        fields = ['id','tipo']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
        def prepend_urls(self):
            return[
                    ]

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        fields =['titulo','usuario','descripcion','link','linkImagen']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()

class CommentsResource(ModelResource):
    class Meta:
        queryset = Comments.objects.all()
        resource_name = 'comments'
        fields =['comentario','usuario_id','post_id']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
