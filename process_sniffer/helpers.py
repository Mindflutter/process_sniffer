import datetime
import os.path as op


def readable_timestamp(timestamp):
    """ Get human readable timestamp from raw integer timestamp
    :param timestamp: (int) raw timestamp
    :return: (str) String in the format "2017-03-16 17:32:05"
    """
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def readable_size(size_in_bytes):
    """ Get human readable size string from raw bytes
    :param size_in_bytes: (int) size in bytes
    :return: (str) String in the format "16.5 MB"
    """
    for size_order in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return "%3.1f %s" % (size_in_bytes, size_order)
        size_in_bytes /= 1024.0
        
        
def get_ports(connections):
    """ Extract ports from psutil connections
    :param connections: psutil.connections
    :return: (list of int) local ports
    """
    # to avoid duplicates initialize a set
    open_ports = set()
    for connection in connections:
        open_ports.add(connection.laddr[1])
    return list(open_ports)


def get_file_info(process_path):
    """ Get created, modified, filesize info on a given file
    :param process_path: (str) File to retrieve info from 
    :return: (dict) Basic info about the file
    """
    if process_path:
        return {'created': readable_timestamp(op.getctime(process_path)),
                'modified': readable_timestamp(op.getmtime(process_path)),
                'size': readable_size(op.getsize(process_path))}
