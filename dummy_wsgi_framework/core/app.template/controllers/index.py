#!/usr/bin/python3
def get_response(environ, start_response, app_config):
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
            "<b>Hello</b>, it is <b><a href='/'>'{app_name}'</a></b> application.",
            "I am a start <i><u>INDEX-page</u></i>.",
        ]
    ).format(app_name=app_config.APP_NAME)
    return [
        bytes(
            response_template.format(content=content), 'utf-8'
        )
    ]
