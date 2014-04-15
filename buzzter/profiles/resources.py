from buzzter.authentication import OAuth20Authentication
from tastypie.authentication import SessionAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ObjectDoesNotExist, MultipleObjectsReturned
from tastypie.utils import trailing_slash
from tastypie import fields
from django.conf.urls import url
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tastypie.http import HttpUnauthorized, HttpForbidden
from models import Profile
from posts.resources import *

class ProfileResource(ModelResource):
    username = fields.CharField(readonly=True, attribute='username', null = True)
    posts = fields.ToManyField('posts.resources.PostResource','posts', full=True)
    class Meta:
        queryset = Profile.objects.all()
        resource_name = 'account'
        fields = ['fotografia']  
        allowed_methods = ['get', 'post', 'put', 'patch']
        include_resource_uri = False
        authorization = DjangoAuthorization()
        authentication = MultiAuthentication(OAuth20Authentication(), SessionAuthentication())
    
    def dehydrate_username(self, bundle):
        return bundle.obj.__unicode__()
    
    def login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        data = self.deserialize(request, request.raw_post_data, format=request.META.get('CONTENT_TYPE', 'application/json'))

        username = data.get('username', '')
        password = data.get('password', '')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return self.create_response(request, {
                    'success': True
                })
            else:
                return self.create_response(request, {
                    'success': False,
                    'reason': 'disabled',
                    }, HttpForbidden )
        else:
            return self.create_response(request, {
                'success': False,
                'reason': 'incorrect',
                }, HttpUnauthorized )

    def logout(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        if request.user and request.user.is_authenticated():
            logout(request)
            return self.create_response(request, { 'success': True })
        else:
            return self.create_response(request, { 'success': False }, HttpUnauthorized)
    
    def get_posts(self, request, **kwargs):
        try:
            bundle = self.build_bundle(data={'pk': kwargs['pk']}, request=request)
            obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        child_resource = PostResource()
        return child_resource.obj_get_list(request).filter(usuario=obj.pk)
    
    def prepend_urls(self):
        return[
            url(r"^(?P<resource_name>%s)/(?P<pk>\w+)/posts%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_posts'), name="api_get_children"),
            url(r"^(?P<resource_name>%s)/login%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('login'), name="api_login"),
            url(r'^(?P<resource_name>%s)/logout%s$' % (self._meta.resource_name, trailing_slash()), self.wrap_view('logout'), name='api_logout'),]
            
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
