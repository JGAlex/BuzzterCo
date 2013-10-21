# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from django.conf.urls import patterns, url
from posts import views

urlpatterns = patterns('',
                        url(r'^(?P<title>\w+)/$',views.PostView,name='posts'),
                       
                        )
