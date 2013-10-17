# -*- coding: utf-8 -*-

__author__="t4r0"
__date__ ="$16-oct-2013 20:14:31$"

from django.conf.urls import patterns, url

from profiles import views 

urlpatterns = patterns('', 
                        url(r'^(?P<user_name>\w+)/$', views.ProfileView, name='profile')
                )