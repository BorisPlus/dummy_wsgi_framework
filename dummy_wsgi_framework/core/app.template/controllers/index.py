#!/usr/bin/python3
import os
import sys

dummy_wsgi_framework_module_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)


def controller_response(environ, start_response, app_config):
    if environ:
        pass  # Lets ignore PyCharm warning about not usage
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [
        bytes(
            "<b>Привет. Я стартовая страница приложения \"%s\"." % app_config.APP_ROOT_DIR_NAME
            , 'utf-8'
        )
    ]
