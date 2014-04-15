from buzzter.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ObjectDoesNotExist, MultipleObjectsReturned
from tastypie import fields
from django.conf.urls import url
from django.contrib.auth.models import User
from posts.resources import *

class UserResource(ModelResource):
    picture = fields.CharField(readonly=True, attribute='picture', null = True) 
    country = fields.CharField(readonly=True, attribute='country', null = True)
    flag = fields.CharField(readonly=True, attribute='flag', null = True)
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        allowed_methods = ['get', 'post', 'put', 'patch']
        fields = ['date_joined','first_name','last_name','is_staff', 'username']       
        detail_uri_name = 'username'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication() 
        
    def dehydrate_picture(self, bundle):
        return '/media/' + str(bundle.obj.profile.fotografia)
    
    def dehydrate_country(self, bundle):
        return bundle.obj.profile.pais    
    
    def dehydrate_flag(self, bundle):
        return bundle.obj.profile.getFlag()
    
    def get_posts(self, request, **kwargs):
        try:
            bundle = self.build_bundle(data={'username':kwargs['username']}, request=request)
            obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this uri")
        child_resource = PostResource()
        return child_resource.get_list(request, usuari = obj.usuario)
        
    def prepend_urls(self):
        return [
            url(r'^user/(?P<username>\w+)/$', self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
            url(r'^user/(?P<username>\w+)/posts/$', self.wrap_view('get_posts'), name='user_get_posts'),]
