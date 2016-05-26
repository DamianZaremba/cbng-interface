from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
import django.contrib.auth.views as auth_views
from django.views.generic import RedirectView
from .views import (signup, profile)
import nexus
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^cluebotng/admin/', include(admin.site.urls)),
    url(r'^cluebotng/nexus/', include(nexus.site.urls)),
    url(r'^cluebotng/report/', include('cbng_report.urls')),
    url(r'^cluebotng/review/', include('cbng_review.urls')),
    url(r'^cluebotng/signup$', signup),
    url(r'^cluebotng/login$', RedirectView.as_view(url='/login/mediawiki')),
    url(r'^cluebotng/logout$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^cluebotng/profile/?$', profile, name='profile'),
    url('^', include('social.apps.django_app.urls', namespace='social')),
    url(r'^cluebotng$', RedirectView.as_view(url='/report'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.extend([
        url(r'^__debug__/', include(debug_toolbar.urls))
    ])

'''
Handle internal errors
'''
handler400 = 'cbng_interface.views.bad_request'  # noqa
handler403 = 'cbng_interface.views.permission_denied'  # noqa
handler404 = 'cbng_interface.views.four_oh_four'  # noqa
handler500 = 'cbng_interface.views.five_hundred'  # noqa
