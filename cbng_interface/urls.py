from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/?$', auth_views.login),
    url(r'^logout/?$', auth_views.login),
    url(r'^oauth-callback/?$', auth_views.login),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
