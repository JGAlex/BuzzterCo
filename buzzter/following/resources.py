__author__="Jorge Quijivix <<j.or.alq@gmail.com>>"
__date__ ="$12/03/2014 11:45:22 PM$"


from tastypie.resources import ModelResource
from following.models import Follower, Following

class FollowerResource(ModelResource):
    class Meta:
        queryset = Follower.objects.all()
        resource_name = 'follower'
        fields = ['usuario']
        authorization = DjangoAuthorizacion()
        authentication = Oauth20Authenticaction()
        
class FollowerResource(ModelResource):
	class Meta:
            queryset = Following.objects.all()
            resource_name = 'following'
            fields = ['usuario']
            authorization = DjangoAuthorizacion()
            authentication = Oauth20Authenticaction()
