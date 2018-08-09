#!/usr/bin/python3
# uri_request_template: controller.py
uri_templates = {
    '/homework_rebuke': 'homework_rebuke.py',
    '/string_functions': 'string_functions.py',
    '/string_methods': 'string_methods.py',
    '': 'index.py',
    'other': 'index.py',
    'error_404': 'error_404.py',
}


def get_uri_template(request_uri):
    return uri_templates.get(request_uri, uri_templates.get("%s" % request_uri.rstrip('/'), 'other'))
