from buzzter.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ObjectDoesNotExist, MultipleObjectsReturned
from tastypie import fields
from tastypie.http import *
from django.conf.urls import url
from django.contrib.auth.models import User
from posts.resources import *
from django.contrib.auth import authenticate, login, logout
from tastypie.http import HttpUnauthorized, HttpForbidden
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.paginator import Paginator
from countries.models import Country

class UserResource(ModelResource):
    picture = fields.CharField(readonly=True, attribute='picture', null = True) 
    country = fields.CharField(readonly=True, attribute='country', null = True)
    flag = fields.CharField(readonly=True, attribute='flag', null = True)
    followers = fields.IntegerField(attribute='followers_count', null=True)
    following = fields.IntegerField(attribute='following_count', null=True)
    
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        allowed_methods = ['get', 'post', 'put']
        fields = ['date_joined','first_name','last_name','is_staff', 'username']       
        detail_uri_name = 'username'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
        filtering={
            'first_name':ALL,
            'last_name':ALL,
            'username':ALL,
            'is_staff':ALL,
        }
        
    def dehydrate_followers(selfs,bundle):
        return bundle.obj.profile.followers.count()
    
    def dehydrate_following(selfs,bundle):
        return bundle.obj.profile.followings.count()
    
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


    def get_followers(self, request, **kwargs):
        try:
            bundle = self.build_bundle(data={'username':kwargs['username']}, request=request)
            obj = self.cached_obj_get(bundle = bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDosNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resorce is found at this uri")

        res = UserResource()
        objects = []

        for _user in obj.profile.followers.all():
            bundle = res.build_bundle(obj = _user, request = request)
            bundle = res.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {'objects': objects}
        res.log_throttled_access(request)
        return res.create_response(request, object_list)

    def get_following(self, request, **kwargs):
        try:
            bundle = self.build_bundle(data={'username':kwargs['username']}, request=request)
            obj = self.cached_obj_get(bundle = bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDosNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resorce is found at this uri")

        res = UserResource()
        objects = []

        for _user in obj.profile.followings.all():
            bundle = res.build_bundle(obj = _user, request = request)
            bundle = res.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {'objects': objects}
        res.log_throttled_access(request)
        return res.create_response(request,object_list)

    def prepend_urls(self):
        return [
            url(r'^user/(?P<username>\w+)/$', self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
            url(r'^user/(?P<username>\w+)/posts/$', self.wrap_view('get_posts'), name='user_get_posts'),
            url(r'^user/(?P<username>\w+)/followers/$', self.wrap_view('get_followers'), name='user_get_followers'),
            url(r'^user/(?P<username>\w+)/following/$', self.wrap_view('get_following'), name='user_get_followings'),
            ]
