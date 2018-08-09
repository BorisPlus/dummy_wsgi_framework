#!/usr/bin/python3
uri_templates = {
    '/string_functions': 'string_functions.py',
    '/string_methods': 'string_methods.py',
    '/': 'index.py'
}

uri_templates.update(dict(other='index.py'))
uri_templates.update({'404': '404.py'})


def get_uri_template(request_uri):
    return uri_templates.get(request_uri, 'other')
