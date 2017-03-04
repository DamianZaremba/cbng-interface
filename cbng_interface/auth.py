from urlparse import urlparse

import jwt
import re
import requests
import requests_oauthlib
from django.conf import settings
from social.backends.oauth import BaseOAuth1
from social.exceptions import AuthFailed


class MediaWikiOAuth(BaseOAuth1):
    name = 'mediawiki'
    ID_KEY = 'username'
    AUTHORIZATION_URL = r'https://en.wikipedia.org/w/index.php?title=Special%3AOAuth%2Fauthorize'
    REQUEST_TOKEN_URL = r'https://en.wikipedia.org/w/index.php?title=Special%3AOAuth%2Finitiate'
    ACCESS_TOKEN_URL = r'https://en.wikipedia.org/w/index.php?title=Special%3AOAuth%2Ftoken'
    IDENTITY_URL = r'https://en.wikipedia.org/w/index.php?title=Special%3AOAuth%2Fidentify'
    REQUIRES_EMAIL_VALIDATION = False
    ACCESS_TOKEN_METHOD = 'POST'

    def get_user_details(self, response):
        if 'blocked' in response and response['blocked']:
            raise AuthFailed('User is blocked')

        return {
            'username': response.get('username', ''),
            'email': response.get('email', ''),
            'fullname': response.get('username', ''),
            'first_name': response.get('username', ''),
            'last_name': '',
        }

    def user_data(self, access_token, *args, **kwargs):
        return self._get_user_token(access_token.get('oauth_token'),
                                    access_token.get('oauth_token_secret'))

    def _get_user_token(self, token, secret):
        (identity, authz_header) = self._get_identity(token, secret)

        # Verify the issuer matches the request domain
        issuer = urlparse(identity['iss']).netloc
        expected_domain = urlparse(self.IDENTITY_URL).netloc
        if not issuer == expected_domain:
            raise Exception('Unexpected issuer (%s != %s)' %
                            (issuer, expected_domain))

        # Verify that the response nonce matches the request nonce
        request_nonce = re.search(
            r'oauth_nonce="(.*?)"', authz_header).group(1)
        if identity['nonce'] != request_nonce:
            raise Exception('Replay attack detected (%s != %s)' %
                            (identity['nonce'], request_nonce))

        return identity

    def _get_identity(self, token, secret):
        # Request the JWT
        r = requests.get(url=self.IDENTITY_URL,
                         auth=requests_oauthlib.OAuth1(client_key=settings.SOCIAL_AUTH_MEDIAWIKI_KEY,
                                                       client_secret=settings.SOCIAL_AUTH_MEDIAWIKI_SECRET,
                                                       resource_owner_key=token,
                                                       resource_owner_secret=secret))

        # Decode the JWT
        try:
            identity = jwt.decode(r.content, settings.SOCIAL_AUTH_MEDIAWIKI_SECRET,
                                  audience=settings.SOCIAL_AUTH_MEDIAWIKI_KEY,
                                  algorithms=["HS256"],
                                  leeway=10.0)
        except jwt.InvalidTokenError as e:
            raise Exception(
                'An error occurred while trying to read identity', e)

        return (identity, r.request.headers['Authorization'])
