#!/usr/bin/python3
import os
import sys

dummy_wsgi_framework_module_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)


def get_response(environ, start_response, app_config, **kwargs):
    if environ and kwargs:
        pass  # Lets ignore PyCharm warning about not usage
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    response_template = """
        <center>
        {content}
        </center>
    """
    content = "<br>".join(
        [
            "",
            "<b>Hello</b>, it is <b><a href='/'>'{app_name}'</a></b> application.",
            "",
            "",
            "I am a start <i><u>INDEX-page</u></i>.",
            "I have a <a href='/random_list/'><i>LIST-page</i></a> with list of random values ",
            "with theirs VIEW-pages."
        ]
    ).format(app_name=app_config.APP_NAME)
    return [
        bytes(
            response_template.format(content=content)
            , 'utf-8'
        )
    ]
