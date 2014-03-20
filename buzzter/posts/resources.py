from tastypie.resources import ModelResource
from posts.models import PostType, Post, Comments
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from buzzter.authentication import OAuth20Authentication
from django.conf.urls import url

class PostTypeResource(ModelResource):
    posts = fields.ToManyField('posts.resources.PostResource','posts', null=True)
    class Meta:
        queryset = PostType.objects.all()
        resource_name = 'type'
        fields = ['tipo']
        detail_uri_name='tipo'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
        def prepend_urls(self):
            return[url(r'(?P<resource_name>%s)/(?P<tipo>\w+)/$' % self._meta.resource_name, self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
                    url(r"^(?P<resource_name>%s)/(?P<username>\w+)/posts%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_posts'), name="api_get_children"),
                    ]

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        fields =['titulo','descripcion','link','linkImagen']
        detail_uri_name='titulo'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
        def prepend_urls(self):
            return[url(r'(?P<resource_name>%s)/(?P<titulo>\w+)/$' % self._meta.resource_name, self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
                    ]

class CommentsResource(ModelResource):
    class Meta:
        queryset = Comments.objects.all()
        resource_name = 'comments'
        fields =['comentario','usuario_id','post_id']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
