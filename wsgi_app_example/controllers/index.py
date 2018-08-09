#!/usr/bin/python3
def controller_response(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [
        b"<b>I am INDEX page. So, HELLO!!!</b> <br>"
        b"See: <br>"
        b" * <a href='./homework_rebuke'>homework rebuke</a> - controller without using HTML-file of view<br>"
        b" * <a href='./string_methods'>string methods</a> - with using HTML-file of view (string_methods.html)<br>"
        b" * <a href='./string_functions'>string functions</a> - with lost HTML-file of view<br>"
        b" * or <a href='./a_priori_bad_way'>a priori bad way</a> - bad links and uri routes<br>"
    ]
