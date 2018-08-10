import os


def render_view_or_404(controller_file, views_dir, environ, start_response):
    view_file_name = os.path.basename(controller_file).rstrip('.py')
    view_path = os.path.join(views_dir, '%s.html' % view_file_name)
    if os.path.exists(view_path):
        start_response('200 OK', [('Content-Type', 'text/html')])
        with open(view_path, 'rb') as f:
            response_body = f.read()
            print(response_body)
            return [response_body]
    start_response('404 Not found', [('Content-Type', 'text/html')])
    return [
        bytes("Missing view HTML-file<br> "
              "Try to create file '%s'"
              "<br>"
              "<br>"
              "<a href='/'>go to start page</a>" % view_path
              , 'utf8')
    ]


