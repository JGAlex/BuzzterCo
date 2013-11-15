from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from posts.views import now
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buzzter.views.home', name='home'),
    # url(r'^buzzter/', include('buzzter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^', include('profiles.urls')),
    url(r'^Login/', 'django.contrib.auth.views.login',
                            {'template_name':'profiles/login.html'}, name = 'login'),
    url(r'^Logout/', 'django.contrib.auth.views.logout_then_login', name = 'logout'),
    url(r'^Posts/', include('posts.urls'), name='posts'),
    url(r'^Now/', now ,name="Now"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
    url(r'^Messages/',include('messages.urls'),name='messages'),
    #url(r'^Rate/', include('rating.urls'), name='rates'),
)
