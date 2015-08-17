from social.backends.oauth import BaseOAuth1


class MediaWikiOAuth(BaseOAuth1):
    name = 'mediawiki'
    BASE_URL = 'https://en.wikipedia.org'
    AUTHORIZATION_URL = '%s/wiki/Special:OAuth/authorize' % BASE_URL
    REQUEST_TOKEN_URL = '%s/w/index.php?title=Special%3AOAuth%2Finitiate' % (
        BASE_URL)
    REQUIRES_EMAIL_VALIDATION = False
    ACCESS_TOKEN_METHOD = 'POST'
