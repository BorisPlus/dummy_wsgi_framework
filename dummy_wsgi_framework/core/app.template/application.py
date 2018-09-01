#!/usr/bin/python3
import os
import sys

dummy_wsgi_framework_module_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)

from dummy_wsgi_framework.core.dispatchers import controllers_dispatcher

# UNCOMMENT THIS
# from path_of_app import config as app_config
if 0:
    app_config = None  # Ignore PyCharm warning


def application(environ, start_response):
    return controllers_dispatcher(environ, start_response, app_config)
