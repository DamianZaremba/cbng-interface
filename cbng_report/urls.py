import views
from django.conf.urls import url, include
from tastypie.api import Api
from .api import (CommentResource,
                  ReportResource)

v1_api = Api(api_name='v1')
v1_api.register(CommentResource())
v1_api.register(ReportResource())

urlpatterns = [
    url(r'^$', views.home),
    url(r'^list/?$', views.list),
    url(r'^(?P<id>\d+)/?$', views.report),
    url(r'^(?P<revert_id>\d+)/status/(?P<status_id>\d)/?$',
        views.report_status_change),
    url(r'^api/', include(v1_api.urls)),
]
