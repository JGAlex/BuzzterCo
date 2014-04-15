from buzzter.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ObjectDoesNotExist, MultipleObjectsReturned
from tastypie import fields
from django.conf.urls import url
from django.contrib.auth.models import User
from posts.resources import *
import pdb

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
        res = PostResource()
        list = Post.objects.filter(usuario = obj)
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
    
    
    def prepend_urls(self):
        return [
            url(r'^user/(?P<username>\w+)/$', self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
            url(r'^user/(?P<username>\w+)/posts/$', self.wrap_view('get_posts'), name='user_get_posts'),
            url(r'^user/(?P<username>\w+)/followers/$', self.wrap_view('get_followers'), name='user_get_followers'),
            url(r'^user/(?P<username>\w+)/following/$', self.wrap_view('get_following'), name='user_get_followings'),]
