import django.contrib.auth.views as auth_views
import nexus
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.signals import user_logged_in
from django.views.generic import RedirectView
from django.views.static import serve
from .utils import (create_api_token,
                    map_user_rights,
                    map_preferences)
from .views import (signup, profile)

admin.autodiscover()
nexus.autodiscover()

urlpatterns = [
    url(r'^cluebotng/admin/', include(admin.site.urls)),
    url(r'^cluebotng/nexus/', include(nexus.site.urls)),
    url(r'^cluebotng/report/', include('cbng_report.urls')),
    url(r'^cluebotng/review/', include('cbng_review.urls')),
    url(r'^cluebotng/signup/?$', signup),
    url(r'^cluebotng/login/?$', RedirectView.as_view(url='/cluebotng/login/mediawiki')),
    url(r'^cluebotng/logout/?$', auth_views.logout, {'next_page': '/cluebotng/'}, name='logout'),
    url(r'^cluebotng/profile/?$', profile, name='profile'),
    url(r'^cluebotng/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^cluebotng/?$', RedirectView.as_view(url='/cluebotng/report/')),
    url(r'^cluebotng/static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.extend([
        url(r'^cluebotng/__debug__/', include(debug_toolbar.urls))
    ])

'''
Handle internal errors
'''
handler400 = 'cbng_interface.views.bad_request'  # noqa
handler403 = 'cbng_interface.views.permission_denied'  # noqa
handler404 = 'cbng_interface.views.four_oh_four'  # noqa
handler500 = 'cbng_interface.views.five_hundred'  # noqa

'''
Fire signals
'''
user_logged_in.connect(create_api_token)
user_logged_in.connect(map_user_rights)
user_logged_in.connect(map_preferences)
