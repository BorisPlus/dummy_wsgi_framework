#!/usr/bin/python3
import sys
import os


dummy_wsgi_framework_module_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)
from dummy_wsgi_framework.app.config import (
    APP_ROOT_DIR_NAME,
)


def controller_response(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [
        bytes(
            "<b>I am INDEX page of application \"%s\". So, HELLO!!!</b> <br>"
            "See: <br>"
            " * <a href='./homework_rebuke'>homework rebuke</a> - controller without using HTML-file of view, "
            " but use russian alphabet<br>"
            " * <a href='./string_methods'>string methods</a> - with using HTML-file of view (string_methods.html)<br>"
            " * <a href='./string_functions'>string functions</a> - with lost HTML-file of view<br>"
            " * or <a href='./a_priori_bad_way'>a priori bad way</a> - bad links and uri routes<br>"
            "" % APP_ROOT_DIR_NAME.upper()
            , 'utf-8'
        )
    ]
