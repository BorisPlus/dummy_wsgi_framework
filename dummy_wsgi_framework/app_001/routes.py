#!/usr/bin/python3
# uri_request_template: controller.py
DEFAULT_TEMPLATE = 'default'
ERROR_404 = 'default'
uri_routes = {
    '': 'index.py',
    DEFAULT_TEMPLATE: 'index.py',
    ERROR_404: 'error_404.py',
}


def get_controller_by_uri(request_uri):
    return uri_routes.get(
        request_uri, uri_routes.get(
            "%s" % request_uri.rstrip('/'),
            DEFAULT_TEMPLATE
        )
    )
