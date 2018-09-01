#!/usr/bin/python3
def controller_response(environ, start_response, app_config):
    if environ:
        pass  # Lets ignore PyCharm warning about not usage
    if app_config:
        pass  # Lets ignore PyCharm warning about not usage
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [
        bytes(
            "<h2>Частые ошибки в домашнем задании:</h2>"
            "<ul>"
            "    <li>неполный ридми;</li>"
            "    <li>непонятные названия (переменных, функций, модулей, проекта);</li>"
            "    <li>все функции в одном файле;</li>"
            "    <li>лишние классы;</li>"
            "    <li>не исправленные баги в коде;</li>"
            "    <li>неправильная декомпозиция функций;</li>"
            "    <li>отсутвие базовой обработки пользовательских данных;</li>"
            "    <li>лишние комментарии.</li>"
            "</ul>"
            "<br>"
            "<a href='/'>Перейти на стартовую страницу.</a>"
            , 'utf-8'
        )
    ]
