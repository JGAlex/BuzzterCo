from buzzter.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ObjectDoesNotExist, MultipleObjectsReturned
from tastypie.utils import trailing_slash
from tastypie import fields
from django.conf.urls import url
from django.contrib.auth.models import User
from models import Profile
from posts.resources import *

class ProfileResource(ModelResource):
    username = fields.CharField(readonly=True, attribute='username', null = True)
    posts = fields.ToManyField('posts.resources.PostResource','posts', null=True)
    class Meta:
        queryset = Profile.objects.all()
        resource_name = 'account'
        fields = ['fotografia']  
        allowed_methods = ['get', 'post', 'put', 'patch']
        include_resource_uri = False
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()    
    
    def dehydrate_username(self, bundle):
        return bundle.obj.__unicode__()
    
    def prepend_urls(self):
        return[
    url(r"^(?P<resource_name>%s)/(?P<username>\w+)/posts%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_posts'), name="api_get_children"),]
class UserResource(ModelResource):
    profile = fields.ToOneField(ProfileResource, 'profile', related_name='user', full=True)
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        allowed_methods = ['get', 'post', 'put', 'patch']
        fields = ['date_joined','first_name','last_name','is_staff']       
        detail_uri_name = 'username'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication() 
            
    def get_profile(self, request, **kwargs):
        try:
            bundle = self.build_bundle(data={'username': kwargs['username']}, request=request)
            obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this URI.")

        child_resource = ProfileResource()
        return child_resource.get_detail(request, id=obj.pk)
        
    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>%s)/(?P<username>\w+)/$' % self._meta.resource_name, self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
            url(r"^(?P<resource_name>%s)/(?P<username>\w+)/profile%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_profile'), name="api_get_children"),]
