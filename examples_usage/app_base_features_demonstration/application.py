#!/usr/bin/python3
import os
import sys

dummy_wsgi_framework_module_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)

from dummy_wsgi_framework.core.dispatchers import get_controller_response
from examples_usage.app_base_features_demonstration import config as app_config


def application(environ, start_response):
    return get_controller_response(environ, start_response, app_config)
