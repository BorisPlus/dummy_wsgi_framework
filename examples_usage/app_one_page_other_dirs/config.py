#!/usr/bin/python3
import os

APP_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_ROOT_DIR_NAME = os.path.basename(APP_ROOT_DIR)
APP_NAME = 'Example: One-page (other dirs)'
APP_VIEWS_DIR = os.path.join(APP_ROOT_DIR, 'other_sub_dir_for_views', 'views')
APP_CONTROLLERS_DIR = os.path.join(APP_ROOT_DIR, 'other_sub_dir_for_controllers', 'controllers')
