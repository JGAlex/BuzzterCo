from tastypie.resources import ModelResource
from posts.models import PostType, Post, Comments
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from buzzter.authentication import OAuth20Authentication
from django.conf.urls import url

class CommentsResource(ModelResource):
    user_uri = fields.CharField(readonly=True, attribute='user_uri', null=True)
    user = fields.CharField(readonly=True, attribute='user', null=True)
    class Meta:
        queryset = Comments.objects.all()
        resource_name = 'comments'
        fields =['comentario','fecha']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
    
    def dehydrate_user_uri(self,bundle):
        return '/v1/user/'+str(bundle.obj.usuario)+'/'
    
    def dehydrate_user(self,bundle):
        return str(bundle.obj.usuario)


class PostResource(ModelResource):
    user_uri=fields.CharField(readonly=True, attribute='user_uri', null=True)
    user = fields.CharField(readonly=True, attribute='user', null=True)
    comments = fields.IntegerField(readonly=True, attribute='comments',null=True)
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'posts'
        fields =['titulo','descripcion','link','linkImagen','fecha','rating','tags']
        allowed_methods=['get','post','put','patch']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def dehydrate_user_uri(self,bundle):   
        return '/v1/user/'+str(bundle.obj.usuario)+'/'
    
    def dehydrate_user(self,bundle):
        return str(bundle.obj.usuario)
    
    def dehydrate_comments(self,bundle):
        return bundle.obj.comentarios.count()
    
    def get_comments(self,request, **kwargs):
        try:
            bundle = self.build_bundle(data={'pk':kwargs['pk']}, request=request)
            obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this uri")
        res= CommentsResource()
        list = obj.comentarios.all()
        objects = []
        for comments in list:
            bundle = res.build_bundle(obj=comments, request=request)
            bundle = res.full_dehydrate(bundle)
            objects.append(bundle)
        object_list={
            'objects':objects
        }
        res.log_throttled_access(request)
        return res.create_response(request, object_list)
        
    def prepend_urls(self):
        return[
            url(r'^post/(?P<pk>\d+)/$', self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
            url(r'^post/(?P<pk>\d+)/comments/$', self.wrap_view('get_comments'),name='post_comments_detail'),
            ]
                
        
