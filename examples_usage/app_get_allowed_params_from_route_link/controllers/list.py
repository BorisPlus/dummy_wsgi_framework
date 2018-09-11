#!/usr/bin/python3
import os
import sys
import random

dummy_wsgi_framework_module_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)


def random_hex_string_generator(size=6, chars='0123456789ABCDEF'):
    return ''.join(random.choice(chars) for _ in range(size))


def get_response(environ, start_response, app_config, **kwargs):
    if environ:
        pass  # Lets ignore PyCharm warning about not usage
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    random_dict = {i: random_hex_string_generator() for i in range(30)}
    random_dict_str = ''
    for i in random_dict:
        random_dict_str += (' - <a href="/view_random/?id={id}&value={value}"><b>view</b></a>'
                            ' with get params id={id} and value={value}<br>').format(
            id=i,
            value=random_dict.get(i)
        )
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
            "I am a <i><u>LIST-page</u></i>",
            "with list of random values (just refresh me) ",
            "with theirs VIEW-pages."
            "",
            "",
            "",
            "{list_at_page}",
        ]
    ).format(
        app_name=app_config.APP_NAME,
        list_at_page=random_dict_str
    )
    return [
        bytes(
            response_template.format(content=content)
            , 'utf-8'
        )
    ]
