from cbng_interface.api import BaseModelResource
from .models import (Beaten,
                     Comment,
                     Report,
                     Vandalism)


class BeatenResource(BaseModelResource):
    class Meta(BaseModelResource.BaseMeta):
        queryset = Beaten.objects.all()


class CommentResource(BaseModelResource):
    class Meta(BaseModelResource.BaseMeta):
        queryset = Comment.objects.all()


class ReportResource(BaseModelResource):
    class Meta(BaseModelResource.BaseMeta):
        queryset = Report.objects.all()


class VandalismResource(BaseModelResource):
    class Meta(BaseModelResource.BaseMeta):
        queryset = Vandalism.objects.all()
