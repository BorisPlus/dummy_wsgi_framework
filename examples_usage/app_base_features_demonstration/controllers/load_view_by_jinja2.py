#!/usr/bin/python3
# Realization with Jinja2
from user_def import load_jinja2_view_template as load_view


def get_response(environ, start_response, app_config):
    return load_view(
        environ,
        start_response,
        app_config,
        'load_me.html',
        id=1,
        value=2,
        other=4
    )
