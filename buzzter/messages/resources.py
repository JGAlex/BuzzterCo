__author__="Linda"
__date__ ="$15/03/2014 04:37:23 PM$"

from tastypie.resources import ModelResource
from messages.models import Messages

class MessagesResource(ModelResource):
    class Meta:
        queryset = Messages.objects.all()
        resource_name = 'MessagesResource'
        