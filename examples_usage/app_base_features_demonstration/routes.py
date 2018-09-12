#!/usr/bin/python3
import os
import sys

dummy_wsgi_framework_module_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)

from dummy_wsgi_framework.core.routes import base_routes_of_uri_regexps


routes_of_uri_regexps = [dict(uri_regexp='^/homework_rebuke/$',
                              controller='homework_rebuke.py'),
                         dict(uri_regexp='^/string_methods/$',
                              controller='string_methods.py'),
                         dict(uri_regexp='^/controller_file_does_not_exists/$',
                              controller='controller_file_does_not_exists.py'),
                         dict(uri_regexp='^/controller_with_missing_method/$',
                              controller='controller_with_missing_method.py'),
                         dict(uri_regexp='^/controller_with_missing_view_file/$',
                              controller='controller_with_missing_view_file.py')
                         ] + list(base_routes_of_uri_regexps).copy()
