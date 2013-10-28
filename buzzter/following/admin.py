# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="JGalex"
__date__ ="$20/10/2013 04:38:28 PM$"

from django.contrib import admin
from following.models import Follower, Following

admin.site.register(Follower)
admin.site.register(Following)
