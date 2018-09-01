#!/usr/bin/python3
import sys
import os


dummy_wsgi_framework_module_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if dummy_wsgi_framework_module_path not in sys.path:
    sys.path.append(dummy_wsgi_framework_module_path)


def controller_response(environ, start_response, app_config):
    if environ:
        pass  # Lets ignore PyCharm warning about not usage
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [
        bytes(
            "<b>Привет. Я стартовая страница приложения \"%s\".</b> <br>"
            "Посмотри: <br>"
            " * <a href='./'>'Стартовая страница'</a> - то, что сейчас видите<br>"
            " * <a href='./homework_rebuke'>'Типовые ошибки ДЗ'</a> - контроллер без представления<br>"
            " * <a href='./string_methods' target='_blank'>'Строковые методы'</a> - контроллер с HTML-представления<br>"
            " * <a href='./string_functions'>'Строковые функции'</a> - HTML-представление умышленно отсутствует<br>"
            " * <a href='./a_priori_bad_way'>Нет пути</a> - в Routes соответствия данному URI<br>"
            "" % app_config.APP_NAME
            , 'utf-8'
        )
    ]
