#!/usr/bin/python3
import logging
import os
import subprocess
import sys
from logging import handlers
import psutil

module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if module_path not in sys.path:
    sys.path.append(module_path)
from gitignore.borisplus.utils.cmd import get_command_line_options_and_args


if __name__ == '__main__':

    file_name = os.path.basename(__file__).split('.')[0]
    dir_name = os.path.dirname(__file__)

    rootLogger = logging.getLogger('%s' % file_name)
    rootLogger.setLevel(logging.INFO)
    logFormatter = logging.Formatter("[%(asctime)s] [%(name)s] %(levelname)-8s %(filename)s %(message)s")

    fileHandler = handlers.TimedRotatingFileHandler(
        os.path.join(dir_name, 'logs', '%s.log' % file_name),
        when='midnight',
        interval=1,
        backupCount=7
    )
    fileHandler.setFormatter(logFormatter)
    fileHandler.setLevel(logging.INFO)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    consoleHandler.setLevel(logging.INFO)
    rootLogger.addHandler(consoleHandler)

    # список аргументов командной строки
    options_and_args = get_command_line_options_and_args(
        sys.argv[1:],
        [
            {'option_name': 'action', 'option_value_comment': '<action:{run,stop,status}>',
             'default_value': 'status'},
            {'option_name': 'http_server_host', 'option_value_comment': '<host:{ip_address,dns_name}>',
             'default_value': '127.0.0.1'},
            {'option_name': 'http_server_port', 'option_value_comment': '<port:{uint_number}>',
             'default_value': '8432'},
            {'option_name': 'application', 'option_value_comment': '<full_application_file_path>',
             'default_value': './application.py'},
        ]
    )
    action = options_and_args.get('cmd_options').get('--action')
    application = options_and_args.get('cmd_options').get('--application')
    http_server_port = options_and_args.get('cmd_options').get('--http_server_port')
    http_server_host = options_and_args.get('cmd_options').get('--http_server_host')
    rootLogger.info('LETS RUN ACTION: %s WITH ARGS: %s' % (
        action,
        options_and_args.get('cmd_args'),
    ))

    if action == 'start':
        messages = []
        for pid in psutil.pids():
            p = psutil.Process(pid)
            if len(p.cmdline()) > 1 and 'uwsgi' in p.cmdline() \
                    and application in p.cmdline() and '--http' in p.cmdline() and os.getpid() != pid:
                message = 'WORK WITH PID:"{}" RUN AS:"{}"'.format(
                    pid,
                    ' '.join(['%s' % cmd_p for cmd_p in p.cmdline()])
                )
                messages.append(message)
        if len(messages) == 0:

            command = [
                'uwsgi',
                '--http', '%s:%s' % (http_server_host, http_server_port),
                '--wsgi-file', '%s' % application,
            ]
            rootLogger.info(' '.join(command))
            subprocess.call(command)

        else:
            for message in messages:
                rootLogger.warning(message)

    elif action == 'stop':

        messages = []
        for pid in psutil.pids():
            p = psutil.Process(pid)
            if len(p.cmdline()) > 1 and 'uwsgi' in p.cmdline():
                message = '{} {}'.format(pid, ' '.join(['%s' % cmd_p for cmd_p in p.cmdline()]))
                messages.append(message)
                p.kill()
        if len(messages):
            rootLogger.info('STOPPED', '\n'.join(messages))
        else:
            rootLogger.info('{} IS NOT RUN'.format('uwsgi'))

    elif action == 'status':

        messages = []
        for pid in psutil.pids():
            p = psutil.Process(pid)
            if len(p.cmdline()) > 1 and 'uwsgi' in p.cmdline() and os.getpid() != pid:
                message = 'WORK WITH PID:"{}" RUN AS:"{}"'.format(
                    pid,
                    ' '.join(['%s' % cmd_p for cmd_p in p.cmdline()])
                )
                messages.append(message)
        if len(messages) == 0:
            message = '{} IS NOT RUN'.format('uwsgi')
            rootLogger.info(message)
        else:
            for message in messages:
                rootLogger.info('%s' % message)

    else:

        rootLogger.warning(options_and_args.get('default_message'))
