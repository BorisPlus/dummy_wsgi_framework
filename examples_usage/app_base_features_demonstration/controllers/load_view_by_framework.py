#!/usr/bin/python3
# Framework solution
from dummy_wsgi_framework.core.dispatchers import load_view


def get_response(environ, start_response, app_config):
    return load_view(
        environ,
        start_response,
        app_config,
        'load_me.html',
        id=1,
        value=2,
        other=4
    )
