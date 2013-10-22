# -*- coding: utf-8 -*-

__author__="t4r0"
__date__ ="$16-oct-2013 20:14:31$"

from django.conf.urls import patterns, url
from profiles import views 
from following import views as follow
urlpatterns = patterns('', 
                        url(r'^Login$', 'django.contrib.auth.views.login',
                            {'template_name':'profiles/login.html'}, name = 'login'),
                        url(r'^Logout/$', 'django.contrib.auth.views.logout_then_login', name = 'logout'),
                        url(r'^Accounts/(?P<user_name>\w+)/$', views.ProfileView, name='profile'),
                        url(r'^Edit/$', views.editProfile, name='edit_profile'),
                        url(r'^Following/$', follow.FollowingView, name='following'),
                        url(r'^Followers/$', follow.FollowersView, name='followers'),
                        url(r'^$', views.SignUp.as_view(), name='signup')
                )