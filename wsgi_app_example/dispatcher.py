#!/usr/bin/python3
import os
import importlib
from wsgi_app_example.routes import get_uri_template

root_dir = os.path.dirname(os.path.abspath(__file__))


def application(environ, start_response):
    uri = environ.get('REQUEST_URI')
    template = get_uri_template(uri)
    if not os.path.exists(os.path.join(root_dir, 'controllers', template)):
        template = get_uri_template('error_404')
    controller = importlib.import_module('wsgi_app_example.controllers.%s' % template.rstrip('.py'))
    controller_response = getattr(controller, 'controller_response')
    return controller_response(environ, start_response)
