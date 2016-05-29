from cbng_interface.api import BaseModelResource
from .models import (Edit,
                     EditGroup,
                     Classification)


class EditResource(BaseModelResource):
    class Meta(BaseModelResource.BaseMeta):
        queryset = Edit.objects.all()


class EditGroupResource(BaseModelResource):
    class Meta(BaseModelResource.BaseMeta):
        queryset = EditGroup.objects.all()


class ClassificationResource(BaseModelResource):
    class Meta(BaseModelResource.BaseMeta):
        queryset = Classification.objects.all()
