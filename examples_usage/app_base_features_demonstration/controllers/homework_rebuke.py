#!/usr/bin/python3
def get_response(environ, start_response, app_config):
    if environ:
        pass  # Lets ignore PyCharm warning about not usage
    if app_config:
        pass  # Lets ignore PyCharm warning about not usage
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [
        bytes(
            "<h2>Типовые ошибки в домашних заданиях учащихся курсов:</h2>"
            "<ul>"
            "    <li>неполный README;</li>"
            "    <li>непонятные названия (переменных, функций, модулей, проекта);</li>"
            "    <li>неисправленные ошибки (после проверки преподавателем) в коде;</li>"
            "    <li>неправильная декомпозиция функциональности;</li>"
            "    <li>все функции в одном файле;</li>"
            "    <li>лишние классы;</li>"
            "    <li>отсутвие базовой обработки пользовательских данных;</li>"
            "    <li>лишние комментарии.</li>"
            "</ul>"
            "<br>"
            "<a href='/'>Перейти на стартовую страницу.</a>"
            , 'utf-8'
        )
    ]
