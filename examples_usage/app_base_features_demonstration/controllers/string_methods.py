#!/usr/bin/python3
# import sys
# import os
#
#
# dummy_wsgi_framework_module_path = os.path.dirname(
#     os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# if dummy_wsgi_framework_module_path not in sys.path:
#     sys.path.append(dummy_wsgi_framework_module_path)
from dummy_wsgi_framework.core.dispatchers import get_view_response, resolve_name_by_python_file_name


def get_response(environ, start_response, app_config):
    return get_view_response(
        environ,
        start_response,
        app_config,
        resolve_name_by_python_file_name(__file__, '%s.html')
    )
