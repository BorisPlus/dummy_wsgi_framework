#!/usr/bin/python3
import sys
import os


dummy_wsgi_framework_module_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)
from dummy_wsgi_framework.framework_core.base_functions import render_view_or_404
from dummy_wsgi_framework.app.config import APP_VIEWS_DIR


def controller_response(environ, start_response):
    return render_view_or_404(
        __file__,
        APP_VIEWS_DIR,
        environ,
        start_response
    )
