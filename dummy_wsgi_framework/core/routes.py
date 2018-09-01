#!/usr/bin/python3
from dummy_wsgi_framework.core.exceptions import ControllerFileDoesNotExists, RouteDoesNotExists
import sys
import os

DEFAULT = 'default'
ERROR_404 = 'error_404'
base_path_info_routes = {
    '': 'index.py',
    DEFAULT: 'index.py',
    ERROR_404: 'error_404.py',
}


def get_controller_by_path_info(request_path_info, app_config):
    try:
        if os.path.exists(os.path.join(app_config.APP_ROOT_DIR, 'routes.py')):
            # sys.path.insert(0, app_config.APP_ROOT_DIR)
            if app_config.APP_ROOT_DIR not in sys.path:
                sys.path.insert(0, app_config.APP_ROOT_DIR)
            routes_module = __import__("routes")
            path_info_routes = routes_module.path_info_routes
        else:
            path_info_routes = base_path_info_routes
    except ImportError:
        raise
    controller = base_path_info_routes.get(
        request_path_info, path_info_routes.get(
            "%s" % request_path_info.rstrip('/'),
            None
        )
    )
    if controller is None:
        raise RouteDoesNotExists
    if not os.path.exists(os.path.join(app_config.APP_CONTROLLERS_DIR, controller)):
        raise ControllerFileDoesNotExists
    return controller
