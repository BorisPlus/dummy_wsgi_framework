#!/usr/bin/python3
def controller_response(environ, start_response, app_config, message):
    if environ:
        pass  # Lets ignore not usage PyCharm
    start_response('404 Not found', [('Content-Type', 'text/html; charset=utf-8')])
    return [
        bytes(
            (
                'Ошибка в приложении "%s"<br>'
                '%s<br>'
                '<a href="/">Перейти на стартовую страницу.</a>'
            ) % (
                app_config.APP_NAME,
                message,
            )
            , 'utf-8'
        )
    ]
