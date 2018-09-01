#!/usr/bin/python3
import os
import sys
import base64

dummy_wsgi_framework_module_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)


def controller_response(environ, start_response, app_config):
    if environ:
        pass  # Lets ignore PyCharm warning about not usage
    if environ.get('HTTP_AUTHORIZATION', '').startswith('Basic '):
        login_password_at_b64 = environ.get('HTTP_AUTHORIZATION', '')[6:]
        login_password = base64.b64decode(login_password_at_b64)
        print(login_password)
        if login_password == b'admin:admin':
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
            return [
                bytes(
                    "Привет. <br>"
                    "Я <a href='/index_2'><b>вторая секретная</b></a> страница приложения \"%s\". <br>"
                    "А тут <a href='/index_1'><b>первая секретная</b></a> с другим пролем." % app_config.APP_ROOT_DIR_NAME
                    , 'utf-8'
                )
            ]
    start_response('401 Access Denied', [
        ('Content-Type', 'text/html; charset=utf-8'),
        ('WWW-Authenticate', 'Basic realm="Dummy WSGI Framework"'),
        ('Content-Length', '0'),
    ])
    return b'Basic Auth'
