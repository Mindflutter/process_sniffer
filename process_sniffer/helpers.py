import datetime
import os.path as op


def readable_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def readable_size(size_in_bytes):
    """ """
    for size_order in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return "%3.1f %s" % (size_in_bytes, size_order)
        size_in_bytes /= 1024.0
        
        
def get_ports(connections):
    # get ports from laddrs
    # to avoid duplicates initialize a set
    open_ports = set()
    for connection in connections:
        open_ports.add(connection.laddr[1])
    return list(open_ports)


def get_file_info(process_path):
    if process_path:
        return {'created': readable_timestamp(op.getctime(process_path)),
                'modified': readable_timestamp(op.getmtime(process_path)),
                'size': readable_size(op.getsize(process_path))}
