from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from posts.models import PostType, Post, Comments
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from buzzter.authentication import OAuth20Authentication
from django.conf.urls import url
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.paginator import Paginator
from tastypie.resources import ModelResource, ObjectDoesNotExist, MultipleObjectsReturned

class CommentsResource(ModelResource):
    post_uri = fields.CharField(readonly=True, attribute='post_uri', null=True)
    post_id = fields.IntegerField(readonly=True, attribute='post_id', null=True)
    user_uri = fields.CharField(readonly=True, attribute='user_uri', null=True)
    user = fields.CharField(readonly=True, attribute='user', null=True)
    
    class Meta:
        queryset = Comments.objects.all()
        resource_name = 'comments'
        fields =['id','comentario','fecha']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        paginator_class = Paginator
            
    def dehydrate_user_uri(self,bundle):
        return '/v1/user/'+str(bundle.obj.usuario)+'/'
    
    def dehydrate_user(self,bundle):
        return str(bundle.obj.usuario)
    
    def dehydrate_post_uri(self,bundle):
        return '/v1/posts/'+str(bundle.obj.post.id)+'/'
    
    def dehydrate_post_id(self,bundle):
        return bundle.obj.post.id
    
    def hydrate(self,bundle):
        if not bundle.obj.usuario_id:
            bundle.obj.usuario_id = User.objects.get(username=bundle.data['user']).id
        if not bundle.obj.post_id:
            bundle.obj.post_id = Post.objects.get(id=bundle.data['post_id']).id
        return bundle
    
class PostResource(ModelResource):
    user_uri=fields.CharField(readonly=True, attribute='user_uri', null=True)
    user = fields.CharField(readonly=True, attribute='user', null=True)
    comments = fields.IntegerField(readonly=True, attribute='comments',null=True)
    
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'posts'
        fields =['id','titulo','descripcion','link','linkImagen','fecha','rating','tags']
        allowed_methods=['get','post','put']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        paginator_class = Paginator
        
        filtering = {
            'tags': ALL,
            'titulo': ALL,
            'id': ALL,
        }
                  
    def dehydrate_user_uri(self,bundle):   
        return '/v1/user/'+str(bundle.obj.usuario)+'/'
    
    def dehydrate_user(self,bundle):
        return str(bundle.obj.usuario)
    
    def dehydrate_comments(self,bundle):
        return bundle.obj.comentarios.count()  
    
    def hydrate(self,bundle):
        if not bundle.obj.usuario_id:
            bundle.obj.usuario_id = User.objects.get(username=bundle.data['user']).id
        if not bundle.obj.tipoPublicacion_id:
            bundle.obj.tipoPublicacion_id = PostType.objects.get(tipo=bundle.data['type']).id
        return bundle
    
    def now(self, request, **kwargs):
        bundle = self.build_bundle(request=request)
        res = PostResource()
        list = Post.objects.all()
        objects = []
        for post in list:
            bundle = res.build_bundle(obj=post, request = request)
            bundle = res.full_dehydrate(bundle)
            objects.append(bundle)
        object_list = {   
            'objects':objects
        }
        res.log_throttled_access(request)
        return res.create_response(request, object_list)

    
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
            url(r'^now/$', self.wrap_view('now'),name='now'),
            ]