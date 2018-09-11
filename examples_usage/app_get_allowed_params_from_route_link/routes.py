#!/usr/bin/python3
routes_of_uri_regexps = (
    dict(uri_regexp=r'^/index/$', controller='index.py'),
    dict(uri_regexp=r'^(/random_list/)$', controller='list.py'),
    dict(uri_regexp=r'^(/view_random/\?(id=[0-9]*)&(value=[A-F0-9]*)/)$', controller='view.py'),
    dict(uri_regexp=r'^/$', controller='index.py'),
)
