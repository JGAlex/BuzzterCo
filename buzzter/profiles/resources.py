from buzzter.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ObjectDoesNotExist, MultipleObjectsReturned
from tastypie import fields
from tastypie.http import *
from django.conf.urls import url 
from tastypie.authentication import MultiAuthentication, BasicAuthentication
from django.contrib.auth.models import User
from posts.resources import *
from profiles.models import Profile
from django.contrib.auth import authenticate, login, logout
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
        allowed_methods = ['get','post' ,'put']
        fields = ['date_joined','first_name','last_name','is_staff', 'username']       
        detail_uri_name = 'username'
        authorization = DjangoAuthorization()
        authentication = MultiAuthentication(OAuth20Authentication(),BasicAuthentication())
        
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
        return 'http://www.buzzter.co/media/' + str(bundle.obj.profile.fotografia)
    
    def dehydrate_country(self, bundle):
        return bundle.obj.profile.pais or None
    
    def dehydrate_flag(self, bundle):
        return 'http://www.buzzter.co/' + bundle.obj.profile.getFlag() or None
    
    def hydrate(self,bundle):
        country=bundle.data['country']
        if country:
            bundle.obj.profile.pais_id= Country.objects.get(printable_name=country).iso
            bundle.obj.profile.save()
        return bundle
            
    def create(self, request, **kwargs):
        data = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/json'))
        user = User(username=data['username'], email=data['email'],password=data['password'])
        user.save()
        profile = Profile(usuario = user)
        profile.save()
        if user.profile:
             return self.create_response(request, 'usuario creado con exito')
        else:
         return self.create_response(request, 'No tengo idea de lo que hago')
     
    def login(self, request, **kwargs):
         data = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/json'))
         user = authenticate(username=data['username'], password=data['password'])
         if user is not None:
			login(request,user)
			bundle = self.build_bundle(obj=user, request=request)
			bundle = self.full_dehydrate(bundle)
			return self.create_response(request,bundle)
			
         else:
            return self.create_response(request,"Something went wrong",response_class=HttpBadRequest)
			
    def logout(self,request, **kwargs):
		logout(request)
		return self.create_response(request,"Logout successful")
	
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
            url(r'^register/$', self.wrap_view('create'), name='create_user'),
            url(r'^login/$', self.wrap_view('login'), name='login'),
			url(r'^logout/$', self.wrap_view('logout'), name='logout'),
            ]
