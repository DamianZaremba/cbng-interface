import django.contrib.auth.views as auth_views
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.signals import user_logged_in
from django.views.generic import RedirectView
from django.views.static import serve
from .utils import (create_api_token,
                    map_user_rights,
                    map_preferences,
                    map_reports)
from .views import (signup,
                    profile,
                    generate_api_key,
                    tool_info)

admin.autodiscover()
URL_PREFIX = ('cluebotng-staging' if settings.STAGING_SITE else 'cluebotng')
urlpatterns = [
    url(r'^%s/admin/' % URL_PREFIX, include(admin.site.urls)),
    url(r'^%s/report/' % URL_PREFIX, include('cbng_report.urls')),
    url(r'^%s/signup/?$' % URL_PREFIX, signup, name='signup'),
    url(r'^%s/login/?$' %
        URL_PREFIX, RedirectView.as_view(url='/cluebotng/login/mediawiki')),
    url(r'^%s/logout/?$' % URL_PREFIX, auth_views.logout,
        {'next_page': '/cluebotng/'}, name='logout'),
    url(r'^%s/profile/?$' % URL_PREFIX, profile, name='profile'),
    url(r'^%s/profile/generate_api_key/?$' % URL_PREFIX, generate_api_key),
    url(r'^%s/toolinfo.json$' % URL_PREFIX, tool_info, name='tool-info'),
    url(r'^%s/' %
        URL_PREFIX, include('social.apps.django_app.urls', namespace='social')),
    url(r'^%s/?$' %
        URL_PREFIX, RedirectView.as_view(url='/cluebotng/report/')),
    url(r'^%s/static/(?P<path>.*)$' %
        URL_PREFIX, serve, {'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.extend([
        url(r'^%s/__debug__/' % URL_PREFIX, include(debug_toolbar.urls))
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
user_logged_in.connect(map_reports)
