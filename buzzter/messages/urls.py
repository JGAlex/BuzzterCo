# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Gerson de Leon"
__date__ ="$29/10/2013 07:40:39 AM$"


from django.conf.urls import patterns, url
from messages import views 

urlpatterns = patterns ('',
                        url(r'^(?P<user_name>\w+)/$',views.SendMessage,name= 'messages'),)