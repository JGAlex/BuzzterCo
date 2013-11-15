# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="JGalex"
__date__ ="$10/11/2013 04:21:02 PM$"

from django.conf.urls import patterns, url
from rating import views

urlpatterns = patterns('',
						url(r'^Rates/(?P<postID>\d+)/(?P<valor>\d+)/$',views.RatingView,name='rating'),
						)