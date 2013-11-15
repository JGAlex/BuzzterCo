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
    url(r'^Posts/', include('posts.urls')),
    url(r'^Now/', now ,name="Now"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
    url(r'^Messages/',include('messages.urls'),name="Now"),
    url(r'^Password_Change/$', 
                        'django.contrib.auth.views.password_change', 
                        {'template_name': 'profiles/passwordChange.html'}),
    url(r'^Password_Change/done/$', 
                        'django.contrib.auth.views.password_change_done', 
                        {'template_name': 'profiles/passwordChangeDone.html'}),
    url(r'^Password_Reset/$',
                        'django.contrib.auth.views.password_reset', 
                        {'template_name': 'profiles/passwordReset.html',
                         'email_template_name': 'profiles/passwordResetEmail.html'}),
    url(r'^Password_Reset/done/$', 
                        'django.contrib.auth.views.password_reset_done', 
                        {'template_name': 'profiles/passwordResetDone.html'}),

    url(r'^Reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
                        'django.contrib.auth.views.password_reset_confirm', 
                        {'template_name': 'profiles/passwordResetConfirm.html'}),
    url(r'^Reset/done/$', 
                        'django.contrib.auth.views.password_reset_complete', 
                        {'template_name': 'profiles/passwordResetComplete.html'}),

)
