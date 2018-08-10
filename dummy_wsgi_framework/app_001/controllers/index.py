#!/usr/bin/python3
import sys
import os

dummy_wsgi_framework_module_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)
from dummy_wsgi_framework.app_001.config import (
    APP_ROOT_DIR_NAME,
)


def controller_response(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [
        bytes(
            "<b>I am INDEX page of application \"%s\". So, HELLO!!!</b>" % APP_ROOT_DIR_NAME.upper()
            , 'utf-8'
        )
    ]
