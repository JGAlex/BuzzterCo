from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from profiles.resources import ProfileResource, UserResource
from posts.resources import PostTypeResource,PostResource,CommentsResource
from following.resources import FollowerResource, FollowingResource
admin.autodiscover()

profileResource = ProfileResource()
api = Api(api_name='v1')
api.register(PostTypeResource())
api.register(PostResource())
api.register(CommentsResource())
api.register(ProfileResource())
api.register(UserResource())
api.register(FollowerResource())
api.register(FollowingResource())
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buzzter.views.home', name='home'),
    # url(r'^buzzter/', include('buzzter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/',include(admin.site.urls)),
    url(r'^auth/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^', include(api.urls)),   
)
