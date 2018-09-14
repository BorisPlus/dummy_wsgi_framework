# Your self realization
from dummy_wsgi_framework.core.dispatchers import decorate_loaded_view_function_for_response


@decorate_loaded_view_function_for_response
def yourself_load_view_function(view_path, **kwargs):
    with open(view_path, 'rb') as f:
        response_body = f.read()
        for k in kwargs:
            response_body = response_body.replace(("{{ %s }}" % k).encode(), str(kwargs[k]).encode())
    return response_body


def get_response(environ, start_response, app_config):
    return yourself_load_view_function(
        environ,
        start_response,
        app_config,
        'load_me.html',
        id=1,
        value=2,
        other=4
    )
