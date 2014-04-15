__date__ ="$12/03/2014 11:45:22 PM$"


from tastypie.resources import ModelResource
from following.models import Follower, Following
from buzzter.authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields

class FollowerResource(ModelResource):
    user_uri=fields.CharField(readonly=True, attribute='user', null=True)

    class Meta:
        queryset = Follower.objects.all()
        resource_name = 'follower'
        fields = ['fotografia', 'usuario', 'pais']
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
        
class FollowingResource(ModelResource):
	class Meta:
            queryset = Following.objects.all()
            resource_name = 'following'
            fields = ['fotografia', 'usuario', 'pais']
            detail_uri_name='usuario'
            allowed_methods=['get','post','put','patch']
            include_resource_uri=False
            authorization = DjangoAuthorization()
            authentication = OAuth20Authentication()

def get_followers(self, request, **kwargs):
    try:
        bundle = self.build_bundle(data={'username':kwargs['username']}, request=request)
        obj = self.cached_obj_get(bundle = bundle, **self.remove_api_resource_names(kwargs))
    except ObjectDosNotExist:
        return HttpGone()
    except MultipleObjectsReturned:
        return HttpMultipleChoices("More than one resorce is found at this uri")

    list = obj.followers.all()
    objects = []

    for user in list:
        package = self.build_bundle(obj = user, request = request)
        package = self.full_dehydrate(bundle)
        objects.append(bundle)
    object_list = {'objects': objects}
    self.log_throttled_access(request)
    return self.create_response(request,object_list)





