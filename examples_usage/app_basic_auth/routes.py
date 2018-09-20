#!/usr/bin/python3
routes_of_uri_regexps = (
    dict(uri_regexp=r'^/index_1/$', controller='first_secret_page.py'),
    dict(uri_regexp=r'^/index_2/$', controller='second_secret_page.py'),
    dict(uri_regexp=r'^/$', controller='first_secret_page.py'),
)
