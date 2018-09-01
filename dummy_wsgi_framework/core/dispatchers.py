#!/usr/bin/python3
# import importlib
import os
import sys

# dummy_wsgi_framework_module_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# if dummy_wsgi_framework_module_path not in sys.path:
#     sys.path.append(dummy_wsgi_framework_module_path)
from dummy_wsgi_framework.core.routes import get_controller_by_path_info
from dummy_wsgi_framework.core.exceptions import (
    ControllerFileDoesNotExists,
    RouteDoesNotExists,
    ViewDoesNotExists,
    BadTermUsage
)
from dummy_wsgi_framework.core.controllers import error404


def __resolve_name_by_python_file_name(file_name):
    if file_name.endswith('.py'):
        return file_name[:-3]
    raise BadTermUsage('Невозможно установить имя модуля по файлу "%s".' % file_name)


def controllers_dispatcher(environ, start_response, app_config):
    path_info = environ.get('PATH_INFO')
    try:
        controller_file = get_controller_by_path_info(path_info, app_config)
        if app_config.APP_CONTROLLERS_DIR not in sys.path:
            sys.path.insert(0, app_config.APP_CONTROLLERS_DIR)
        controller_module = __import__(
            __resolve_name_by_python_file_name(controller_file)
        )
        # раньше не передавал app_config, решил так гибче
        return controller_module.controller_response(environ, start_response, app_config)
    except RouteDoesNotExists:
        return error404.controller_response(
            environ, start_response, app_config,
            message='Маршрут для PATH_INFO "%s" в приложении "%s" не существует.' % (
                path_info, app_config.APP_NAME
            )
        )
    except ControllerFileDoesNotExists:
        return error404.controller_response(
            environ, start_response, app_config,
            message='Файл объявленного в маршрутах контроллера с PATH_INFO "%s" приложения "%s" не сущетсвует.' % (
                path_info, app_config.APP_NAME
            )
        )
    except ViewDoesNotExists:
        return error404.controller_response(
            environ, start_response, app_config,
            message=sys.exc_info()[1]
        )
    except BadTermUsage:
        return error404.controller_response(
            environ, start_response, app_config,
            message=sys.exc_info()[1]
        )


def views_dispatcher(environ, start_response, app_config, controller_file):
    if environ:
        pass  # Lets ignore PyCharm warning about not usage
    view_path = None
    view_file_name = None
    try:
        view_file_name = '%s.html' % __resolve_name_by_python_file_name(os.path.basename(controller_file))
        view_path = os.path.join(app_config.APP_VIEWS_DIR, view_file_name)
        with open(view_path, 'rb') as f:
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
            response_body = f.read()
            return [response_body]
    except BadTermUsage:
        raise  # передадим дальше
    except FileNotFoundError:
        print('FileNotFoundError HANDLED')
        raise ViewDoesNotExists(
            "Отсутствует HTML-файл представления '%s' "
            "в папке '%s' <br>" % (
                view_path,
                view_file_name
            )
        )
