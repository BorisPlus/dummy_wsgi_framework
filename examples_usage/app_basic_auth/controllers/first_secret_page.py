#!/usr/bin/python3
import base64


def get_response(environ, start_response, app_config):
    if environ:
        pass  # Lets ignore PyCharm warning about not usage
    if environ.get('HTTP_AUTHORIZATION', '').startswith('Basic '):
        login_password_at_b64 = environ.get('HTTP_AUTHORIZATION', '')[6:]
        login_password = base64.b64decode(login_password_at_b64)
        if login_password == b'user:user':
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
            return [
                bytes(
                    "Hello. <br>"
                    "I am <a href='/index_1'><b>first</b></a> secret page of application \"%s\". <br>"
                    "There is <a href='/index_2'><b>second</b></a> secret page "
                    "with differ password." % app_config.APP_NAME
                    , 'utf-8'
                )
            ]
    start_response('401 Access Denied', [
        ('Content-Type', 'text/html; charset=utf-8'),
        ('WWW-Authenticate', 'Basic realm="Dummy WSGI Framework"'),
        ('Content-Length', '0'),
    ])
    return b'Basic Auth'
