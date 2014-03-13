from buzzter.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from tastypie import fields
from django.conf.urls import url
from django.contrib.auth.models import User
from models import Profile

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resourcer_name = 'user'
        fields = ['username','date_joined','first_name','last_name','is_staff']
        detail_uri_name = 'username'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>%s)/(?P<username>\w+)/$' % self._meta.resource_name, self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),        ]

class ProfileResource(ModelResource):
    user = fields.ToOneField(UserResource, 'user', full=True)
    class Meta:
        queryset = Profile.objects.all()
        resource_name = 'account'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>%s)/(?P<username>[\w\d_.-]+)/$' % self._meta.resource_name, self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
        ]