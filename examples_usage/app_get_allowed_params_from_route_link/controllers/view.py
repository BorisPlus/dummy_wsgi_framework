#!/usr/bin/python3
import os
import sys

dummy_wsgi_framework_module_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)


def get_response(environ, start_response, app_config, **kwargs):
    if environ:
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
            "I am a <i><u>VIEW-page</u></i>",
            "with allowed params 'id' and 'value'.",
            "",
            "I get params:",
            "{params}"
        ]
    ).format(
        app_name=app_config.APP_NAME,
        params='<ul>{li_list}</ul>'.format(
            li_list=''.join(['<li><u><i>%s</i></u>: %s</li>' % (p, kwargs[p]) for p in sorted(kwargs)])
        )
    )
    return [
        bytes(
            response_template.format(content=content)
            , 'utf-8'
        )
    ]
