#!/usr/bin/python3
# import sys
# import os


# dummy_wsgi_framework_module_path = os.path.dirname(
#     os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# if dummy_wsgi_framework_module_path not in sys.path:
#     sys.path.append(dummy_wsgi_framework_module_path)
from dummy_wsgi_framework.core.dispatchers import views_dispatcher


def controller_response(environ, start_response, app_config):
    return views_dispatcher(
        environ,
        start_response,
        app_config,
        __file__
    )
