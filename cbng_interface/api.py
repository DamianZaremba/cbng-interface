'''
Core API (tastypie) settings
'''
from tastypie import resources
from tastypie.authentication import (MultiAuthentication,
                                     SessionAuthentication,
                                     ApiKeyAuthentication)
from tastypie.authorization import DjangoAuthorization


class BaseModelResource(resources.ModelResource):
    class BaseMeta:
        def __init__(self, *args, **kwargs):
            if not self.resource_name:
                self.resource_name = self.__class__.__name__.replace('Resource', '').lower()

        max_limit = 0
        authorization = DjangoAuthorization()
        authentication = MultiAuthentication(SessionAuthentication(),
                                             ApiKeyAuthentication())
        always_return_data = True
