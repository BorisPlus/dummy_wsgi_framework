#!/usr/bin/python3
from dummy_wsgi_framework.core.routes import base_routes_of_uri_regexps

routes_of_uri_regexps = tuple(
    [
        dict(uri_regexp='^/homework_rebuke/$',
             controller='homework_rebuke.py'),
        dict(uri_regexp='^/string_methods/$',
             controller='string_methods.py'),
        dict(uri_regexp='^/controller_file_does_not_exists/$',
             controller='controller_file_does_not_exists.py'),
        dict(uri_regexp='^/controller_with_missing_method/$',
             controller='controller_with_missing_method.py'),
        dict(uri_regexp='^/controller_with_missing_view_file/$',
             controller='controller_with_missing_view_file.py'),
        dict(uri_regexp='^/load_view_by_framework/$',
             controller='load_view_by_framework.py'),
        dict(uri_regexp='^/load_view_by_yourself/$',
             controller='load_view_by_yourself.py'),
        dict(uri_regexp='^/load_view_by_jinja2/$',
             controller='load_view_by_jinja2.py')
    ] + list(base_routes_of_uri_regexps).copy())
