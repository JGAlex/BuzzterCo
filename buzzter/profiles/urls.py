# -*- coding: utf-8 -*-

__author__="t4r0"
__date__ ="$16-oct-2013 20:14:31$"

from django.conf.urls import patterns, url
from profiles import views 
from following import views as follow
urlpatterns = patterns('', 
                        url(r'^Accounts/(?P<user_name>\w+)/$', views.ProfileView, name='profile'),
                        url(r'^Edit/$', views.editProfile, name='edit_profile'),
                        url(r'^Following/$', follow.FollowingView, name='following'),
                        url(r'^Followers/$', follow.FollowersView, name='followers'),
                        url(r'^Follow/(?P<username>\w+)/$', 'following.views.Follow', name='follow'),
                        url(r'^Unfollow/(?P<username>\w+)/$', 'following.views.Unfollow', name='unfollow'),
                        url(r'^Publications/$', 'profiles.views.MyPublications'),
                        url(r'^Rating/$', 'profiles.views.MyRatings'),
                        url(r'^Me/$', 'profiles.views.AboutMe'),
                        url(r'^$', views.SignUp, name='signup')
                        )