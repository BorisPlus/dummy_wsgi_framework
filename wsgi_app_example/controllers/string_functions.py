#!/usr/bin/python3
import os
from wsgi_app_example.dispatcher import root_dir


def controller_response(environ, start_response):
    view_file_name = os.path.basename(__file__).rstrip('.py')
    view_path = os.path.join(root_dir, 'views', '%s.html' % view_file_name)
    print(view_path)
    if os.path.exists(view_path):
        start_response('200 OK', [('Content-Type', 'text/html')])
        with open(view_path, 'rb') as f:
            response_body = f.read()
            print(response_body)
            return [response_body]
    start_response('424 Failed Dependency', [('Content-Type', 'text/html')])
    return [bytes("You forgot create view HTML-file<br> "
                  "Try to create file 'views/%s.html'"
                  "<br>"
                  "<br>"
                  "<a href='/'>go to start page</a>" % view_file_name
                  , 'utf8')]
