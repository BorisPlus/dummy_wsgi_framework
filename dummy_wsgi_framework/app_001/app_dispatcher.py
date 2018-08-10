#!/usr/bin/python3
import importlib
import sys
import os

dummy_wsgi_framework_module_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)
from dummy_wsgi_framework.app_001.routes import get_controller_by_uri, ERROR_404
from dummy_wsgi_framework.app_001.config import (
    APP_ROOT_DIR_NAME,
    APP_ROOT_DIR
)


def application(environ, start_response):
    uri = environ.get('REQUEST_URI')
    controller_file = get_controller_by_uri(uri)
    if not os.path.exists(os.path.join(APP_ROOT_DIR, 'controllers', controller_file)):
        controller_file = get_controller_by_uri(ERROR_404)
    controller = importlib.import_module('dummy_wsgi_framework.%s.controllers.%s' % (
        APP_ROOT_DIR_NAME, controller_file.rstrip('.py')))
    controller_response_function = getattr(controller, 'controller_response')
    return controller_response_function(environ, start_response)
