#!/usr/bin/python3
from dummy_wsgi_framework.core.routes import base_path_info_routes

path_info_routes = base_path_info_routes.copy()
path_info_routes.update(
    **{
        '/homework_rebuke/': 'homework_rebuke.py',
        '/string_functions/': 'string_functions.py',
        '/string_methods/': 'string_methods.py',
        '/controller_with_missing_view_file/': 'controller_with_missing_view_file.py'
    }
)
