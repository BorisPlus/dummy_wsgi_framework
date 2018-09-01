#!/usr/bin/python3
from dummy_wsgi_framework.core.routes import base_uri_routes

uri_routes = base_uri_routes.copy()
uri_routes.update(
    **{
        '/homework_rebuke': 'homework_rebuke.py',
        '/string_functions': 'string_functions.py',
        '/string_methods': 'string_methods.py',
        '/controller_with_missing_view_file': 'controller_with_missing_view_file.py'
    }
)
