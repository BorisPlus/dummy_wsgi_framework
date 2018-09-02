#!/usr/bin/python3
import os
import sys

dummy_wsgi_framework_module_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)

from dummy_wsgi_framework.core.routes import base_path_info_routes

path_info_routes = base_path_info_routes.copy()
path_info_routes.update(
    **{
        '/homework_rebuke/': 'homework_rebuke.py',
        '/string_methods/': 'string_methods.py',
        '/controller_file_does_not_exists/': 'controller_file_does_not_exists.py',
        '/controller_with_missing_view_file/': 'controller_with_missing_view_file.py',
    }
)
