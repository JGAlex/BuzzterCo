# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from django.conf.urls import patterns, url
from posts import views

urlpatterns = patterns('',
                        url(r'^(?P<id>\d+)/$',views.PostView,name='posts'),
                        url(r'^New/(?P<tipoP>\w+)/$',views.newPost,name='newPost'),
                        url(r'^Delete/(?P<id>\d+)/$',views.deletePost,name='delete'),
                        )
