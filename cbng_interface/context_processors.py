from django.conf import settings

def staging_site(request):
    return {
        'is_staging_site': (settings.STAGING_SITE or settings.DEBUG),
    }