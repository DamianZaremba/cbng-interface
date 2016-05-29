from django.conf.urls import url, include
import views
from tastypie.api import Api
from .api import (EditResource,
                  EditGroupResource,
                  ClassificationResource)

v1_api = Api(api_name='v1')
v1_api.register(EditResource())
v1_api.register(EditGroupResource())
v1_api.register(ClassificationResource())

urlpatterns = [
    url(r'^$', views.about),
    url(r'^reviewer/?$', views.reviewer),
    url(r'^stats/?$', views.stats),

    url(r'^admin/?$', views.admin),
    url(r'^admin/edits/?$', views.admin_edits),
    url(r'^admin/edits/(?P<edit_id>\d+)/?$', views.admin_edit),

    url(r'^japi/next/?$', views.japi_next),
    url(r'^japi/score/(?P<edit_id>\d+)/(?P<score_id>\d+)?$', views.japi_score),

    url(r'^api/', include(v1_api.urls)),
]
