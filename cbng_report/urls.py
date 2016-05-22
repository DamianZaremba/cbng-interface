from django.conf.urls import url, include
import views
from tastypie.api import Api
from .api import (BeatenResource,
                  CommentsResource,
                  ReportsResource,
                  VandalismResource)


v1_api = Api(api_name='v1')
v1_api.register(BeatenResource())
v1_api.register(CommentsResource())
v1_api.register(ReportsResource())
v1_api.register(VandalismResource())

urlpatterns = [
    url(r'^$', views.home),
    url(r'^list$', views.list),
    url(r'^(?P<id>\d+)$', views.report),
    url(r'^(?P<revert_id>\d+)/status/(?P<status_id>\d)$',
        views.report_status_change),
    url(r'^api/', include(v1_api.urls)),
]
