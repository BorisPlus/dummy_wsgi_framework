from wsgi_app_example.routes import get_uri_template
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def application(environ, start_response):
    print(environ)
    uri = environ.get('REQUEST_URI')
    template = get_uri_template(uri)
    if not os.path.exists(os.path.join('controllers', template)):
        template = get_uri_template('404')
    __import__('wsgi_app_example.controllers.%s' % template.rstrip('.py'))

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]
