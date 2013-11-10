# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Krn_mt"
__date__ ="$18-oct-2013 15:35:44$"

from django.contrib import admin
from posts.models import Post, PostType, Comments

admin.site.register(Post)
admin.site.register(PostType)
admin.site.register(Comments)