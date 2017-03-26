#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil
import json

from helpers import readable_timestamp, get_file_info, get_ports


OUTPUT_FILE = 'process_info.txt'


def main():
    """ Entry point """
    output = {}
    for process in psutil.process_iter():
        info = process.as_dict(attrs=['pid', 'username', 'create_time', 'exe', 'cmdline', 'connections'])
        output[process.pid] = {'username': info['username'],
                               'start_time': readable_timestamp(info['create_time']),
                               'exe_path': info['exe'],
                               'exe_info': get_file_info(info['exe']),
                               'cmdline_args': info['cmdline'],
                               'open_ports': get_ports(info['connections']),
                               'children': True if process.children() else False}

    with open(OUTPUT_FILE, 'w') as outfile:
        outfile.write(json.dumps(output, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
