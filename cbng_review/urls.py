from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.about),
    url(r'^reviewer/?$', views.reviewer),
    url(r'^stats/?$', views.stats),

    url(r'^japi/next/?$', views.japi_next),
    url(r'^japi/score/?$', views.japi_score),
]
