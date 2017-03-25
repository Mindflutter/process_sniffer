import psutil
import datetime


output = {}

def readable_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


for process in psutil.process_iter():
    info = process.as_dict(attrs=['pid', 'username', 'create_time', 'exe', 'cmdline', 'connections'])
    output[process.pid] = {'username': info['username'],
                   'create_time': readable_timestamp(info['create_time']),
                   'exe_path': info['exe'],
                   'exe_info': None,
                   'cmdline_args': info['cmdline'],
                   'open_ports': None}
print output


def get_file_info(process_path):
    # os module: created, modified, filesize
    pass


def get_ports(connections):
    # get ports from laddrs
    pass

# def main():
#     pass
#
# if __name__ == '__main__':
#     main()
