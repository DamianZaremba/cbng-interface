from cbng_interface.api import BaseModelResource
from .models import (Beaten,
                     Comments,
                     Reports,
                     Vandalism)


class BeatenResource(BaseModelResource):

    class Meta(BaseModelResource.BaseMeta):
        queryset = Beaten.objects.all()


class CommentsResource(BaseModelResource):

    class Meta(BaseModelResource.BaseMeta):
        queryset = Comments.objects.all()


class ReportsResource(BaseModelResource):

    class Meta(BaseModelResource.BaseMeta):
        queryset = Reports.objects.all()


class VandalismResource(BaseModelResource):

    class Meta(BaseModelResource.BaseMeta):
        queryset = Vandalism.objects.all()
