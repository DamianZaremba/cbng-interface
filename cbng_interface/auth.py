from social.backends.oauth import BaseOAuth1


class MediaWikiOAuth(BaseOAuth1):
    name = 'mediawiki'
    AUTHORIZATION_URL = 'https://en.wikipedia.org/wiki/Special:OAuth/authorize'
    REQUEST_TOKEN_URL = 'https://en.wikipedia.org/w/index.php?title=Special%3AOAuth%2Finitiate'
    REQUIRES_EMAIL_VALIDATION = False
    ACCESS_TOKEN_METHOD = 'POST'
