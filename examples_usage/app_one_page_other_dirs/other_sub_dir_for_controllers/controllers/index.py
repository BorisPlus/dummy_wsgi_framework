#!/usr/bin/python3
from dummy_wsgi_framework.core.dispatchers import get_view_response


def get_response(environ, start_response, app_config):
    return get_view_response(
        environ,
        start_response,
        app_config,
        'index.html'
    )
