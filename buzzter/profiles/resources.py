from tastypie.resources import ModelResource
from profiles.models import Profile

class ProfilesResource(ModelResource):
    class Meta:
        querysey = Profile.objects.all()
        resource_name = 'ProfilesResource'