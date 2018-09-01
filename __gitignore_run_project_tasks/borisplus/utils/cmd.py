#!/usr/bin/python3
import os
import sys
import getopt
import logging


def get_command_line_options_and_args(argv, wait_options):
    result_cmd_options = dict()
    cmd_suffix = ''
    options_names_set = set()
    options_names_dict = dict()
    for wait_option in wait_options:
        options_names_set.add('%s=' % wait_option.get('option_name'))
        if '--%s' % wait_option.get('option_name') not in options_names_dict:
            options_names_dict['--%s' % wait_option.get('option_name')] = wait_option.get('default_value', '')
            cmd_suffix += ' --%s=%s' % (wait_option.get('option_name'), wait_option.get('option_value_comment'))
    default_message = 'FORMAT: %s%s' % (
        os.path.basename(__file__), cmd_suffix
    )
    try:
        options, result_cmd_args = getopt.getopt(argv, "", list(options_names_set))
    except getopt.GetoptError:
        logging.info(argv)
        logging.info(default_message)
        sys.exit(2)

    for opt, arg in options:
        if opt == '--help':
            logging.info(default_message)
            if opt in options_names_dict:
                logging.info(default_message)
            sys.exit()
        elif opt in options_names_dict and opt not in result_cmd_options:
            result_cmd_options[opt] = arg
        else:
            pass

    for option_name in options_names_dict:
        if option_name in result_cmd_options:
            continue
        result_cmd_options[option_name] = options_names_dict[option_name]
    return dict(
        cmd_options=result_cmd_options,
        cmd_args=result_cmd_args,
        default_message=default_message
    )


if __name__ == '__main__':
    pass
