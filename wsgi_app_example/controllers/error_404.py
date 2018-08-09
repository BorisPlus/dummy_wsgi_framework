#!/usr/bin/python3
def controller_response(environ, start_response):
    start_response('404 Not found', [('Content-Type', 'text/html')])
    return [b"<html><h1>It is 404, my baby... :(</h1><br>"
            b"<a href='./'>go UP</a><br> <a href='/'>go to start page</a> </html>"]
