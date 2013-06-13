from retry import *
from helpers import *


class RetryException(Exception):
    pass

xrdp_settings = {'path': '/usr/local/sbin/xrdp', 'host': '0.0.0.0', 'port': '3389'}
xrdp_sesman_settings = {'path': '/usr/local/sbin/xrdp-sesman', 'host': '127.0.0.1', 'port': '3550'}
secsvc_path = 'xrdp-secsvc'
x11rdp_path = 'X11rdp'


@retry(ExceptionToCheck=RetryException)
def check_xrdp(path, host, port):
    print ">> Checking xrdp (main)..."
    if is_process(path):
        if is_tcp_listen(host, port):
            print ">> xrdp up and running"
        else:
            print ">> xrdp test failed"
            kill_process(path)
            raise RetryException
    else:
            print ">> xrdp test failed"
            rm_files("/var/run/xrdp.pid")
            #TODO: rm_files("/tmp/.xrdp/xrdp-?")
            kill_xrdp_sesman()
            start_process(path)
            check_xrdp_sesman(**xrdp_sesman_settings)
            raise RetryException


@retry(ExceptionToCheck=RetryException)
def check_xrdp_sesman(path, host, port):
    print ">> Checking xrdp-sesman..."
    if is_process(path):
        if is_tcp_listen(host, port):
            print "[OK]"
        else:
            print ">> xrdp test failed"
            kill_xrdp_sesman()
            raise RetryException
    else:
        rm_files("/var/run/xrdp-sesman.pid")
        rm_files("/tmp/.xrdp/xrdp-sesman*")
        # TODO: Cleanup unused X11rdp locks
        start_process(path)
        raise RetryException


def kill_xrdp_sesman():
    print ">> killing xrdp-sesman..."
    kill_process("startwm.sh")
    sleep(5)
    kill_process("xrdp")
    kill_process("xrdp-sesman")
    kill_process(secsvc_path)
    kill_process(x11rdp_path)


if __name__ == "__main__":
    try:
        check_xrdp(**xrdp_settings)
    except RetryException: pass

