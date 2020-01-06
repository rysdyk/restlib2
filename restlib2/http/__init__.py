# from django.core.handlers.wsgi import STATUS_CODE_TEXT
import http
from restlib2.structures import AttrDict

http.client.responses.setdefault(422, 'UNPROCESSABLE ENTITY')

# http://tools.ietf.org/html/rfc6585
http.client.responses.setdefault(428, 'PRECONDITION REQUIRED')
http.client.responses.setdefault(429, 'TOO MANY REQUESTS')
http.client.responses.setdefault(431, 'REQUEST HEADER FIELDS TOO LARGE')
http.client.responses.setdefault(511, 'NETWORK AUTHENTICATION REQUIRED')

# http://tools.ietf.org/html/draft-tbray-http-legally-restricted-status-02
http.client.responses.setdefault(451, 'UNAVAILABLE FOR LEGAL REASONS')

# Invert dict for reference by name
codes = AttrDict('HTTP Status Codes',
    [(y, x) for x, y in http.client.responses.items()])


# PATCH Method introduced - http://tools.ietf.org/html/rfc5789
methods = AttrDict('HTTP Methods',
    GET = 'GET',
    HEAD = 'HEAD',
    OPTIONS = 'OPTIONS',
    POST = 'POST',
    PUT = 'PUT',
    DELETE = 'DELETE',
    PATCH = 'PATCH',
)
