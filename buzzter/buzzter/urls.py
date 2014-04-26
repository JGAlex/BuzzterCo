from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from profiles.resources import UserResource
from posts.resources import PostResource,CommentsResource

admin.autodiscover()

api = Api(api_name='v1')
api.register(PostResource())
api.register(CommentsResource())
api.register(UserResource())
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
