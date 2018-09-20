#!/usr/bin/python3
from dummy_wsgi_framework.core.dispatchers import get_view_response, resolve_name_by_python_file_name


def get_response(environ, start_response, app_config):
    return get_view_response(
        environ,
        start_response,
        app_config,
        resolve_name_by_python_file_name(__file__, '%s.html')
    )
