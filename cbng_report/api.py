from cbng_interface.api import BaseModelResource
from .models import (Comment,
                     Report)


class CommentResource(BaseModelResource):

    class Meta(BaseModelResource.BaseMeta):
        queryset = Comment.objects.all()


class ReportResource(BaseModelResource):

    class Meta(BaseModelResource.BaseMeta):
        queryset = Report.objects.all()
