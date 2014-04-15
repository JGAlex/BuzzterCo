from tastypie.resources import ModelResource
from posts.models import PostType, Post, Comments
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from buzzter.authentication import OAuth20Authentication
from django.conf.urls import url

class PostResource(ModelResource):
    user_uri=fields.CharField(readonly=True, attribute='user', null=True)
    
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        fields =['titulo','descripcion','link','linkImagen','fecha','rating','tags']
        detail_uri_name='titulo'
        allowed_methods=['get','post','put','patch']
        include_resource_uri=False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def dehydrate_user_uri(self,bundle):   
        return '/v1/user/'+str(bundle.obj.usuario)+'/'
    
    def get_comments(self,request, **kwargs):
        try:
            bundle = serlf.buil_bundle(ddata={'pk': kwargs['pk']}, request=request)
            obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        child_resource = PostResource()
        return child_resource.obj_get_list(request).filter(usuario=obj.pk)
        

class CommentsResource(ModelResource):
    class Meta:
        queryset = Comments.objects.all()
        resource_name = 'comments'
        fields =['comentario','usuario_id','post_id']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
